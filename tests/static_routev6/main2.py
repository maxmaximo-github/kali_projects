#!/usr/bin/env python3
from datetime import datetime
from subprocess import run
from subprocess import call
from subprocess import STDOUT
from dns import resolver


dictionary_names = {
    "r1.example.com": "AAAA",
    "r41.example.com": "AAAA",
    "r51.example.com": "AAAA"
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
        date_time = datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
        if reply != True:
            print(f" {date_time}  Ping was success to {ipv6_address}")
        else:
            print(f"Ping was not success to {ipv6_address}    {date_time}")


if __name__ == '__main__':
    main()
