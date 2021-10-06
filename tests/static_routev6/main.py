#!/usr/bin/env python3
from dns import resolver
from subprocess import run
from subprocess import call
from subprocess import STDOUT
# from subprocess import CompleteProcess



dictionary_names = {
    "r1.example.com": "AAAA",
    "r41.example.com": "AAAA",
    "r51.example.com": "AAAA",
    "r50.example.com": "AAAA"
}

def main():

    ipv6_addresses = []
    for keys, values in dictionary_names.items():
        try:
            answers = resolver.resolve(keys, values)
            for ip_address in answers:
                ipv6_addresses.append(ip_address)

        except(resolver.NXDOMAIN, resolver.NoAnswer):
            pass

    for ipv6_address in ipv6_addresses:
        command = f"ping -6 -c 4 {ipv6_address} "
        reply = call(command, shell=True, stdout=open('/dev/null', "w"))
        # reply = run(command, capture_output=True).check_returncode()
        # reply = reply.check_returncode()
        if reply != True:
            with open(file="ping.txt", mode="a") as file:
                file.write(f"Ping was success to {ipv6_address}\b\b\b \n")
        else:
            with open(file="ping.txt", mode="a") as file:
                file.write(f"Ping was not success to {ipv6_address}\n")


if __name__ == '__main__':
    main()
