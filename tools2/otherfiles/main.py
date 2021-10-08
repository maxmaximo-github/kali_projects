#!/usr/bin/env  python3


from telnetlib import Telnet


username = "cesar"
password = "cesar"
# host_ipv6_address = "ns1.example.com"

with Telnet(host="ns1.example.com") as telnet_connection:
    telnet_connection.read_until(bytes("Username: ", encoding="ascii"))
    telnet_connection.write(username.encode("ascii") + bytes("\n", encoding="ascii"))

    if password:
        telnet_connection.read_until(bytes("Password: ", encoding="utf-8"))
        telnet_connection.write(password.encode("ascii") + bytes("\n", encoding="ascii"))

    commands_list = [
        "configure terminal", "ip host r5.example.com 2001:db8:cafe::8000",
        "ip host r2.example.com 2001:db8:cafe::900", "end", "terminal lengt 0",
        "show run | section ip host", "exit"
    ]

    for command in commands_list:
        telnet_connection.write(bytes(f" {command} \r\n", encoding="ascii"))

    output = telnet_connection.read_all().decode("ascii")

with open("show_config.txt", mode="w") as file:
    file.write(output)



#     telnet_connection.write(b"terminal lengt 0 \r\n")
#     telnet_connection.write(b"show version \r\n")
    
#     telnet_connection.write(b" exit \r\n")
