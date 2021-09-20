#!/usr/bin/env  python3


from telnetlib import Telnet
from subprocess import popen

hosts_list = [
    "r1.example.com", "ns1.example.com",
    "sw2.example.com", "sw1.example.com"
]

pub_key

for host in hosts_list:

    with Telnet(host=f"{host}") as tel_conn:

        tel_conn.read_until(bytes("Username: ", "ascii"))
        tel_conn.write(bytes("cesar\n", "ascii"))

        tel_conn.red_until(bytes("Password: ", "ascii"))
        tel_conn.write(bytes("cesar\n", "ascii"))
