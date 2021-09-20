#!/usr/bin/env python3


from pyshark import LiveCapture

capture = LiveCapture(interface="eth0", display_filter="dns")


for packet in capture.sniff_continuously():
    try:
        if int(packet.udp.srcport) != 53:
            print(f"Has realizado una consulta para {packet.dns.qry_name}")

        elif int(packet.udp.srcport) == 53:
            print(f"{packet.dns.qry_name} has a RR {packet.dns.aaaa}")

        else:
            continue
        
    except:
        pass


exit()
