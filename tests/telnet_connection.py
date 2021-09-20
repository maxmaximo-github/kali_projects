#!/usr/bin/env python3


from telnetlib import Telnet
from subprocess import popen

rr_names = {
    "r2.example.com": "2001:db8:cafe:2::1",
    "r3.example.com": "2001:db8:cafe:3::1",
    "r4.example.com": "2001:db8:cafe:4::1"

}

with Telnet(host="ns1.example.com") as tel_conn:
    tel_conn.set_debuglevel(3)
    tel_conn.read_until(bytes("Username: ", encoding="ascii"))
    tel_conn.write(bytes("cesar\n", encoding="ascii"))
    tel_conn.read_until(bytes("Password: ", encoding="ascii"))
    tel_conn.write(bytes("cesar\n", encoding="ascii"))

    for keys, values in rr_names.items():
        tel_conn.write(bytes("configure terminal \r\n", encoding="ascii"))
        tel_conn.write(bytes(f"ip host {keys} {values} \r\n", encoding="ascii"))
        tel_conn.write(bytes("exit \r\n", encoding="ascii"))

    tel_conn.write(bytes("terminal leng 0 \r\n", encoding="ascii"))
    tel_conn.write(bytes("show running-config \r\n", encoding="ascii"))
    tel_conn.write(bytes("exit \r\n", encoding="ascii"))

    output = str(tel_conn.read_all(), encoding="ascii")

with open(file="running_config.txt", mode="w") as file:
    file.write(output)
