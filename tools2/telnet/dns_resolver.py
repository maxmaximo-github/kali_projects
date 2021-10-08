#!/usr/bin/env  python3

from dns import resolver

qname_list = [
    "ns1.example.com", "sw1.example.com", "sw2.example.com",
    "r1.example.com", "r2.example.com", "r3.example.com",
    "sw3.example.com", "sw4.example.com"
    ]


aaaa_exist = []
aaaa_not_exist = []
for name in qname_list:
    try:
        answers = resolver.resolve(f"{name}", "AAAA")
        
        for answer in answers:
            aaaa_exist.append(f"Host {name} has a AAAA with {answer}")
    
    except (resolver.NXDOMAIN, resolver.NoAnswer):
        aaaa_not_exist.append(f"Host {name} doesn't AAAA")

aaaa_exist.extend(aaaa_not_exist)

print(f"\n\n")
for i in aaaa_exist:
    print(f"{i}")