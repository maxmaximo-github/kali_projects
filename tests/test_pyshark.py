#!/usr/bin/env python3


from pyshark import FileCapture

capture = FileCapture("1.pcapng", display_filter="dns")

list_dir = dir(capture[13].dns)

for i in list_dir:
    with open(file="dns.txt", mode="a") as file:
        file.write(f"{i}\n")
