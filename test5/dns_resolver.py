#!/usr/bin/env python3

from dns import resolver

for answers in resolver.resolve("r1.example.com", "AAAA"):
    print(f"Host r1.example.com has AAAA with {answers}")

