#!/usr/bin/env  python3

from pathlib import Path
from getpass import getpass

def pubkey_creation(*args):

    for device in devices:
        if (ssh_dir/f"{device}_id_rsa").is_file():


def main():
    global devices
    global ssh_dir

    devices = [
        "ns1.example.com", "r1.example.com", "sw1.example.com",
        "sw2.example.com"
    ]

    ssh_dir = Path(f"{Path.home()}/.ssh")

    username = input("Input username: ")

    while True:
        passphrase = getpass(prompt="Input your passphrase: ")
        if not passphrase:
            confirmation = input(
            "You don't input a passphrase, are you continue?: Y/n ")
            if "y" in confirmation.lower():
                break
        else:
            break
