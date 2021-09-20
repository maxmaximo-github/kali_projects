#!/usr/bin/env python3


from telnetlib import Telnet
from getpass import getpass

try:
    with Telnet(host="ns1.example.com") as telnet_connection:
        telnet_connection.set_debuglevel(3)

except PermissionError:
    print("The host possibly has a firewall activated.")
