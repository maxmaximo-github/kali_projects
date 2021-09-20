#!/usr/bin/env  python3

from getpass import getpass
from sys import exit
from telnetlib import Telnet
from dns import resolver

username = input("Input your username: ")
password = getpass(prompt="Input your password: ")

domain_names = {
    "r3.example.com": "2001:db8:cafe:1::300",
    "r4.example.com": "2001:db8:cafe:1::400",
    "r5.example.com": "2001:db8:cafe:1::500",

}

with Telnet(host="ns1.example.com") as tel_conn:

    # tel_conn.set_debuglevel(3)

    tel_conn.read_until(bytes(f"Username: ", encoding="ascii"))
    tel_conn.write(bytes(f"{username}\n", encoding="ascii"))

    if password:
        tel_conn.read_until(bytes(f"Password: ", encoding="ascii"))
        tel_conn.write(bytes(f"{password}\n", encoding="ascii"))

        for v, k in domain_names.items():
            tel_conn.write(bytes(f"configure terminal \r\n", encoding="ascii"))
            tel_conn.write(bytes(f"ip host {v} {k} \r\n", encoding="ascii"))
            tel_conn.write(bytes(f"exit \r\n", "ascii"))

        
        # tel_conn.write(bytes(f"terminal length 0 \r\n", encoding="ascii"))
        # tel_conn.write(bytes(f"show version \r\n", encoding="ascii"))
        tel_conn.write(bytes(f"exit \r\n", encoding="ascii"))

        print(tel_conn.read_all().decode(encoding="ascii"))

    else:
        print(f"No ingresaste ningun password")
        exit()
        


# for v, k in domain_names.items():

answers = resolver.query("r1.example.com", "AAAA")

for datum in answer:
    print(datum)
