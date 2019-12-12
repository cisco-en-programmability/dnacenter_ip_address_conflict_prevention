# Cisco DNA IPv4 Address Conflict Prevention


This Python script will verify if the use of an IPv4 Address will create a duplicated IPv4 address.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

This script will ask the user to input the following:

- IPv4 address

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

$ python ip_conflict_prevention.py

*Sample output:*


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
