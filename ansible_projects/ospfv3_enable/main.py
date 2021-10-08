#!/usr/bin/env python3


from dns import resolver
from subprocess import call


hostnames_dictionary = {
    "r1.example.com": "AAAA",
    "r41.example.com": "AAAA",
    "r51.example.com": "AAAA"
}

def main():

    addresses = []
    for key, value in hostnames_dictionary.items():
        try:
            answers = resolver.resolve(key, value)
            for address in answers:
                addresses.append(address)

        except (resolver.NMDOMAIN, resolver.NoAnswer):
            pass

    for ip_address in addresses:
        command = f"ping -6 -c 4 {ip_address}"

        reply = call(command, shell=True, stdout=open("/dev/null", "w"))

        if reply != True:
            print(f"Ping was success to {ip_address}")
        else:
            print(f"Ping was not success to {ip_address}")

if __name__ == '__main__':
    main()
