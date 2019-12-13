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


Start of Application "ip_conflict_prevention.py" Run
Input the CLI Template file name (example - "cli.txt"):   cli.txt

The CLI template:

!
interface Loopback65
 ip address 10.93.130.21 255.255.255.255
 !
interface Loopback200
 ip address 10.93.141.67 255.255.255.255
!
interface Tunnel201
 ip address 10.93.140.35 255.255.255.252
 tunnel source Loopback200
 tunnel destination 10.93.140.48
 keepalive
!
router eigrp 123
 network 10.93.140.49 0.0.0.0
!
router eigrp 201
 network 10.93.140.46 0.0.0.0
 redistribute static route-map REMOTE_ACCESS
 exit
!

These valid IPv4 addresses will be configured by this CLI template:
['10.93.130.21', '10.93.141.67', '10.93.140.35']

The IPv4 address  10.93.130.21  is used by this device  PDX-M , interface  GigabitEthernet0/0

The IPv4 address  10.93.141.67  is used by this device  APB026.80DF.6E18 , interface  unknown

The IPv4 address  10.93.140.35  is not used by any network devices
The IPv4 address  10.93.140.35  is used by a client

Deploying the template  cli.txt  will create an IP address conflict


End of Application "path_trace.py" Run

Process finished with exit code 0



**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
