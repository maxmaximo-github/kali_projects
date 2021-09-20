#!/usr/bin/env  python3


from datetime import datetime
from getpass import getpass
from pathlib import Path
from string import ascii_lowercase
from subprocess import run
from telnetlib import Telnet
from threading import Thread
from random import choice



def pubkey_creation(device, data2):
    username, passphrase = data2

    ssh_dir = Path(f"{Path.home()}/.ssh")

    if (ssh_dir/f"{device}_id_rsa").is_file():
        (ssh_dir/f"{device}_id_rsa").unlink()
        (ssh_dir/f"{device}_id_rsa.pub").unlink()

    if not passphrase:
        command = (
        f"ssh-keygen -f {ssh_dir}/{device}_id_rsa -b 4096 " +
        f"-C {username}@{device} -q").split()
        run(command, capture_output=True, input=b"\n")
    else:
        command = (
        f"ssh-keygen -f {ssh_dir}/{device}_id_rsa -b 4096 " +
        f"-C {username}@{device} -P {passphrase} -q").split()
        run(command, capture_output=True)


def telnet_config(device, data):
    ssh_dir = Path(f"{Path.home()}/.ssh")
    path = Path(f"{ssh_dir}/{device}_id_rsa.pub")

    with path.open(mode="r") as file:
        pub_key = file.read()

    sep = []
    for i in range(0, len(pub_key), 72):
        sep.append(pub_key[i:i+72])

    username, password = data
    with Telnet(host=device) as tel_conn:
        tel_conn.read_until(bytes("Username: ", "ascii"))
        tel_conn.write(bytes(f"{username}\n", "ascii"))

        tel_conn.read_until(bytes("Password: ", "ascii"))
        tel_conn.write(bytes(f"{password}\n", "ascii"))

        commands_enable_ssh = [
            "configure terminal", "line vty 0 4", "login local",
            "transport input ssh telnet", "ip domain name example.com",
            "ip ssh version 2", "crypto key generate rsa modulus 4096",
            "ip ssh pubkey-chain",
        ]

        for command in commands_enable_ssh:
            if "ip ssh pubkey-chain" in command:
                tel_conn.write(bytes(f"no {command} \r\n", "ascii"))
                tel_conn.write(bytes(f"{command} \r\n", "ascii"))
                tel_conn.write(bytes(f"username {username} \r\n", "ascii"))
                tel_conn.write(bytes(f"key-string \r\n", "ascii"))
                for i in sep:
                    tel_conn.write(bytes(f"{i}\r\n", "ascii"))
                tel_conn.write(bytes("exit \r\n", "ascii"))
                tel_conn.write(bytes("exit \r\n", "ascii"))
            else:
                tel_conn.write(bytes(f"{command} \r\n", "ascii"))

        tel_conn.write(bytes("end \r\n", "ascii"))
        tel_conn.write(bytes("exit \r\n", "ascii"))

        print(str(tel_conn.read_all(), encoding="ascii"))

    print("Configuration exitosa")


def ThreadConfig(function, devices, data=None):
    threads = []
    for device in devices:
        th = Thread(target=function, args=(device, data))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


def main():

    home = Path.home()
    ssh_dir = Path(f"{home}/.ssh")

    username = input("Give me a username: ")
    password = getpass(prompt="Gime the password: ")
    data = (username, password)

    devices = [
    "ns1.example.com",# "r1.example.com",
    # "sw1.example.com", "sw2.example.com"
    ]

    while True:
        passphrase = getpass(prompt="Give me passphrase: ")
        if not passphrase:
            confirmation = input(
                    "You don't set passphrase, are you sure to continue?: Y/n ")
            if "y" in confirmation.lower():
                break
            else:
                continue
        else:
            break


    data2 = (username, passphrase)

    ThreadConfig(pubkey_creation, devices, data2)
    ThreadConfig(telnet_config, devices, data)

    path = Path(f"{ssh_dir}/config")
    if not path.is_file():
        print("The file doesn't exist.")
        file = Path(f"{ssh_dir}/config")
        file.touch()

    else:
        date_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

        path.rename(f"{ssh_dir}/config_{date_time}")
        file = Path(f"{ssh_dir}/config")
        file.touch()

    lines_config = [
        "Host", "HostName", "User",
        "KexAlgorithms diffie-hellman-group-exchange-sha1",
        "IdentityFile"
    ]

    print(path)

    with path.open(mode="a") as file:
        for device in devices:
            for line in lines_config:
                if "Host" in line:
                    if not "Name" in line:
                        file.write(f"{line} {device}\n")
                    else:
                        file.write(f"\t\t{line} {device}\n")

                elif "KexAlgorithms" in line:
                    file.write(f"\t\t{line}\n")

                elif "User" in line:
                    file.write(f"\t\t{line} {data[0]}\n")

                elif "IdentityFile" in line:
                    file.write(f"\t\t{line} {ssh_dir}/{device}_id_rsa\n\n\n")


if __name__ == "__main__":
    main()
