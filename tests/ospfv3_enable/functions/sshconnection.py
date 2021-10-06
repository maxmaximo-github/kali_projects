#!/usr/bin/env python3

import logging
from netmiko import Netmiko

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


def SSHConnection(**kwargs):

    if "cisco_ios" in kwargs["device_type"]:
        commands = [
            "ipv6 router ospf 1",
            f"router-id {kwargs['router_id']}",
            "default-information originate always"]

        for interface in kwargs["interfaces"]:
            if interface["ospf"]:
                commands.append(f"int {interface['name']}")
                commands.append(f"ipv6 ospf {interface['ospf_id']} area 0")
            else:
                pass

    elif "vyos" in kwargs["device_type"]:
        commands = [
            f"set protocols ospfv3 parameters router-id {kwargs['router_id']}"
        ]
        for interface in kwargs["interfaces"]:
            if interface ["ospf"]:
                commands.append(f"set protocols ospfv3 area 0 " +
                                f"interface {interface['name']}")


    router = {
        "device_type": kwargs["device_type"],
        "host": kwargs["hostname"],
        "username": kwargs["username"],
        "key_file": kwargs["id_rsa"],
        "ssh_config_file": "/home/kali/.ssh/config",
    }


    with Netmiko(**router) as ssh_connection:

        output = ssh_connection.send_config_set(commands, exit_config_mode=False)
        print(output)

        # Save configuration
        if "cisco_ios" in kwargs["device_type"]:
            ssh_connection.save_config()
        else:
            ssh_connection.commit()
