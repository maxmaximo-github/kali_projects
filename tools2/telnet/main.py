#!/usr/bin/env  python3


import telnetlib


ip_address = "2001:db8:cafe:1::500"
user = "cesar"
password = "cesar"


tn = telnetlib.Telnet(host=ip_address)

tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"terminal length 0\r\n")
tn.write(b"show running-config\r\n")
tn.write(b" exit \r\n")

print(tn.read_all().decode("ascii"))
tn.close()
