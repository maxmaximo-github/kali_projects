#!/usr/bin/env python3


from dns import resolver

names_list = [
    "ns1.example.com", "example.example.com", "r1.example.com",
    "sw1.example.com", "sw2.example.com"

]

for name in names_list:
    try:
        answers = resolver.resolve(f"{name}", "AAAA")
        for i in answers:
            print(f"{name}")

    except(resolver.NXDOMAIN, resolver.NoAnswer):
        print(f"No se ha encontrando un registro para {name}")
