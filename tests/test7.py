#!/usr/bin/env  python3


from subprocess import Popen


pub_key = Popen([
        "fold", "-b", "-w 72",
        "/home/kali/.ssh/r1_id_rsa.pub"], shell=False)

with open(file="r1.example.com.pub", mode="w") as file:
    file.write(f"{pub_key}")
