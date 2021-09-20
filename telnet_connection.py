#!/usr/bin/env python3


from telnetlib import Telnet
from getpass import getpass

try:
    record_name = {
        "r2.example.com": "2001:db8:cafe:2::1",
        "r3.example.com": "2001:db8:cafe:3::1",
        "r4.example.com": "2001:db8:cafe:4::1",
        "r5.example.com": "2001:db8:cafe:5::1"
    }

    username = input("Input username: ")
    password = getpass(prompt="Input password: ")
    with Telnet(host="ns1.example.com") as telnet_connection:
        telnet_connection.set_debuglevel(3)
        telnet_connection.read_until(bytes("Username: ", "ascii"))
        telnet_connection.write(bytes(f"{username}\n", "ascii"))
        telnet_connection.read_until(bytes("Password: ", "ascii"))
        telnet_connection.write(bytes(f"{password}\n", "ascii"))

        for key, value in record_name.items():
            telnet_connection.write(bytes("configure terminal \r\n", "ascii"))
            telnet_connection.write(bytes(f"ip host {key} {value} \r\n", "ascii"))
            telnet_connection.write(bytes("exit \r\n", "ascii"))

        telnet_connection.write(bytes("exit \r\n", "ascii"))

        telnet_connection.read_all()

except PermissionError:
    print("The host possibly has a firewall activated.")

except ConnectionRefusedError:
    print("The host doesn't have the service listening.")
