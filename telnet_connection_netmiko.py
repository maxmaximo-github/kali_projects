#!/usr/bin/env  python3


import logging
from netmiko import ConnectHandler

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

device = {
    "host": "ns1.example.com",
    "device_type": "cisco_ios",
    "session_log": "output.txt",
    "verbose": True,
    "key_file": "/home/kali/.ssh/ns1.example.com_id_rsa",
    "ssh_config_file": "/home/kali/.ssh/config",
    # "passphrase": "cesar",
}

with ConnectHandler(**device) as ssh_connection:
    output = ssh_connection.check_enable_mode()
    if output:
        ssh_connection.write_channel("show running-config \n")

    ssh_connection.disconnect()
