#!/usr/bin/env python3

from pathlib import Path
from os import environ
from subprocess import Popen
from subprocess import run
from subprocess import PIPE
from subprocess import STDOUT
from telnetlib import Telnet


HOME_DIR = environ["HOME"]
device = "sw2.example.com"

if not Path(f"{HOME_DIR}/.ssh/{device}_id_rsa").is_file():
    print("The file doesn't exist")
    command = (
        f'ssh-keygen -f {HOME_DIR}/.ssh/{device}_id_rsa -b 4096 ' +
        f'-C cesar@sw2.example.com -P ""').split()
    print(command)
else:
    print("The file exists")
    command = f'ssh-keygen -f {HOME_DIR}/.ssh/{device}_id_rsa -b 4096 -C cesar@sw2.example.com -P "" -y'.split()
run(command, capture_output=True)


# print(output)

"""
with open(file="/home/kali/.ssh/sw2_id_rsa.pub", mode="r") as file:
    pub_key = file.readline()


sep = []
for i in range(0, len(pub_key), 72):
    sep.append(pub_key[i:i+72])

print(sep)

with Telnet(host="sw2.example.com") as tel_conn:

    tel_conn.set_debuglevel(3)
    tel_conn.read_until(bytes("Username: ", "ascii"))
    tel_conn.write(bytes("cesar\n", "ascii"))
    tel_conn.read_until(bytes("Password: ", "ascii"))
    tel_conn.write(bytes("cesar\n", encoding="ascii"))

    tel_conn.write(bytes("configure terminal \r\n", "ascii"))
    tel_conn.write(bytes("ip ssh pubkey-chai \r\n", "ascii"))
    tel_conn.write(bytes("username cesar \r\n", "ascii"))
    tel_conn.write(bytes("key-string \r\n", "ascii"))
    for i in sep:
        tel_conn.write(bytes(i + "\r\n", encoding="ascii"))
    tel_conn.write(bytes("exit \r\n", "ascii"))
    tel_conn.write(bytes("exit \r\n", "ascii"))
    tel_conn.write(bytes("end \r\n", "ascii"))
    tel_conn.write(bytes("exit \r\n", "ascii"))

    print(str(tel_conn.read_all(), encoding="ascii"))
"""
