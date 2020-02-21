#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""



Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import os
import urllib3
from requests.auth import HTTPBasicAuth  # for Basic Auth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

import dnac_apis
import utils
from config import DNAC_PASS, DNAC_USER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def main():
    """
    This sample script will:
     - ask user to input the file name with the CLI template to be configured
     - validate the provided file name exists
     - open the file
     - select the IPv4 addresses to be configured on interfaces
     - validate if the selected IPv4 addresses are valid IPv4 addresses
     - verify if the IPv4 addresses are in use by a network device
     - verify if the IPv4 addresses are in use by a client
     - verify if the IPv4 addresses are reachable
     - deploying the configuration file will create an IPv4 address conflict if any of the above steps fail for one IPv4 address
    """

    print('\n\nStart of Application "ip_conflict_prevention.py" Run')

    # ask user to input the file name with the CLI template to be configured

    # enter and validate the file exists
    while True:
        config_file = input('Input the CLI Template file name (example - "cli_template.txt"):   ')
        if os.path.isfile(config_file):
            break
        else:
            print('File not found')

    # open file with the template
    cli_file = open(config_file, 'r')

    # read the file
    cli_config = cli_file.read()
    print('\nThe CLI template:\n')
    print(cli_config)

    ipv4_address_list = utils.identify_ipv4_address(cli_config)
    print('\nThe CLI template will configure these valid IPv4 addresses:')
    print(ipv4_address_list)

    # get the DNA Center Auth token

    dnac_token = dnac_apis.get_dnac_jwt_token(DNAC_AUTH)

    # check each address against network devices and clients database

    duplicate_ip = False
    for ipv4_address in ipv4_address_list:

        # check against network devices interfaces

        device_info = dnac_apis.check_ipv4_network_interface(ipv4_address, dnac_token)
        if device_info[0] == 'Found':
            duplicate_ip = True
            print('\nThe IPv4 address ', ipv4_address, ' is used by this device ', device_info[1], ', ',config
                  device_info[2])
        else:
            print('\nThe IPv4 address ', ipv4_address, ' is not used by any network devices')

            # if IP address no used by network devices continue to check against any hosts

            try:
                client_info = dnac_apis.get_client_info(ipv4_address, dnac_token)
                if client_info:
                    duplicate_ip = True
                    print('The IPv4 address ', ipv4_address, ' is used by a client')
                else:
                    print('The IPv4 address ', ipv4_address, ' is not used by a client')

                    # if IP address not used by a client, continue with the reachability test

                    reachable = utils.ping_return(ipv4_address)
                    if reachable == 'Success':
                        duplicate_ip = True
                        print('The IPv4 address ', ipv4_address, ' is reachable')
                    else:
                        print('The IPv4 address ', ipv4_address, ' is not reachable')
            except:
                pass

    if duplicate_ip:
        print('\nDeploying the template ', config_file, ' will create an IP address conflict')
    else:
        print('\nDeploying the template ', config_file, ' will not create an IP address conflict')

    # end of the application run
    print('\n\nEnd of Application "ip_conflict_prevention.py" Run')


if __name__ == "__main__":
    main()

