# Cisco DNA IPv4 Address Conflict Prevention


This Python script will verify if the use of an IPv4 Address will create a duplicated IPv4 address.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

This app will ask the user to input the following:

- IPv4 address

- It will verify if the provided IPv4 address is a valid address. 
- It will check the current Cisco DNA Center device and client inventories to search for a match of the address.
- It will verify if the address is reachable at the present time


$ python ip_conflict_prevention.py

*Sample output:*

    


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
