#!/usr/bin/env python3

from dns import resolver

dictionary_names = {
    "ns1.example.com": "AAAA",
    "r1.example.com": "AAAA",
    "sw1.example.com": "AAAA",
    "sw2.example.com": "AAAA",
    "r2.example.com": "AAAA",
    "r3.example.com": "AAAA",
    "r4.example.com": "AAAA",
    "r5.example.com": "AAAA",
    "r15.example.com": "AAAA"
}

names_list = []
for keys, values in dictionary_names.items():
    try:
        answers = resolver.resolve(keys, values)

        for ip_address in answers:
           names_list.append(f"Host {keys} has the RR {values} with {ip_address}")


    except(resolver.NXDOMAIN, resolver.NoAnswer):
        names_list.append(f"Host {keys} doesn't {values}")

with open(file="queries.txt", mode="w") as file:
    for name in names_list:
        file.write(f"{name}\n")
