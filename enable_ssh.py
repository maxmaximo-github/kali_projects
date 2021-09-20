#!/usr/bin/env python3

from getpass import getpass
from pathlib import Path
from subprocess import run


def pubkey_creation(*args):

    for device in devices:
        if (ssh_dir/f"{device}_id_rsa").is_file():
            (ssh_dir/f"{device}_id_rsa").unlink()
            (ssh_dir/f"{device}_id_rsa.pub").unlink()


        if not args[-1]:
            command = (
                f"ssh-keygen -f {ssh_dir}/{device}_id_rsa -b 4096 " +
                f"-C {args[0]}@{device} -q").split()
            run(command, capture_output=True, input=b"\n")
        else:
            command = (
                f"ssh-keygen -f {ssh_dir}/{device}_id_rsa -b 4096 " +
                f"-C {args[0]}@{device} -P {args[-1]} -q").split()
            run(command, capture_output=False)



def main():
    global devices
    global ssh_dir

    # global list
    devices = [
        "ns1.example.com", "r1.example.com",
        "sw1.example.com", "sw2.example.com"]
    # global variable
    ssh_dir = Path(f"{Path.home()}/.ssh")

    # device username
    username = input("Input your username: ")

    while True:
        passphrase = getpass(prompt= "Input your passphrase: ")
        if not passphrase:
            confirmation = input(
                "You don't input a passphrase, are you continue?: Y/n ")
            if "y" in confirmation.lower():
                break

        else:
            break

    pubkey_creation(username, passphrase)


if __name__ == "__main__":
    main()
