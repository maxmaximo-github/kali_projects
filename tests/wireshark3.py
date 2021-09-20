#!/usr/bin/env python3


from pyshark import FileCapture

cap = FileCapture("wireshark.pcapng")

for i in range(0, 200):
    try:
        cap[i].show()

    except(KeyError):
        pass

exit()
