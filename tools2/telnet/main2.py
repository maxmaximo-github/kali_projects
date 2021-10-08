#!/usr/bin/env python3


from telnetlib import Telnet

username = "cesar"
password = "cesar"

with Telnet(host="ns1.example.com") as telnet_connection:
    telnet_connection.read_until(bytes("Username: ", encoding="ascii"))

    telnet_connection.write(username.encode("ascii") + bytes("\n", encoding="ascii"))


    if password:
        telnet_connection.read_until(bytes("Password: ", encoding="ascii"))
        telnet_connection.write(password.encode("ascii") + bytes("\n", encoding="ascii"))

    telnet_connection.write(bytes("configure terminal \r\n", encoding="ascii"))
    telnet_connection.write(bytes("ip host r3.example.com 2001:db8:cafe::300 \r\n", encoding="ascii"))
    telnet_connection.write(bytes("end \r\n", encoding="ascii"))
    telnet_connection.write(bytes("show running | section ip host \r\n", encoding="ascii"))
    telnet_connection.write(bytes("exit \r\n", encoding="ascii"))

    print(telnet_connection.read_all().decode("ascii"))