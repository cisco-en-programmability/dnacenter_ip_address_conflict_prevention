# Cisco DNA IPv4 Address Conflict Prevention


This Python script will verify if the use of an IPv4 Address will create a duplicated IPv4 address.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

This sample script will:
     - ask user to input the file name with the CLI template to be configured
     - validate the provided file name exists
     - open the file
     - select the IPv4 addresses to be configured on interfaces
     - validate if the selected IPv4 addresses are valid IPv4 addresses
     - Verify if the IPv4 addresses are:
        - Used by a network device
        - Used by a client
        - Reachable
     - deploying the configuration template will create an IPv4 address conflict if any of the above validations fail for one IPv4 address

Execute the script:

$ python ip_conflict_prevention.py


*Sample output:*

Start of Application "ip_conflict_prevention.py" Run
Input the CLI Template file name (example - "config.txt"):   cli_template.txt

The CLI template:

!
interface Loopback65
 ip address 10.93.130.21 255.255.255.255
 !
interface Loopback200
 ip address 10.93.141.67 255.255.255.255
!
interface Loopback201
 ip address 10.93.140.35 255.255.255.255
!
interface Tunnel201
 ip address 10.93.130.19 255.255.255.252
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

The CLI template will configure these valid IPv4 addresses:
['10.93.130.21', '10.93.141.67', '10.93.140.35', '10.93.130.19']

The IPv4 address  10.93.130.21  is used by this device  PDX-M ,  GigabitEthernet0/0

The IPv4 address  10.93.141.67  is used by this device  AP682C.7B4C.0510 ,  

The IPv4 address  10.93.140.35  is not used by any network devices
The IPv4 address  10.93.140.35  is used by a client

The IPv4 address  10.93.130.19  is not used by any network devices
The IPv4 address  10.93.130.19  is not used by a client
The IPv4 address  10.93.130.19  is not reachable

Deploying the template  config.txt  will create an IP address conflict


End of Application "ip_conflict_prevention.py" Run

Process finished with exit code 0


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
