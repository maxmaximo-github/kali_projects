#!/usr/bin/env python3


from functions.jsonformat import JSONDataImport
from functions.sshconnection import SSHConnection


def main():

    data = JSONDataImport()

    if data:
        devices = [device for device in data["devices"]]


        for device in devices:
            SSHConnection(**device)


    else:
        print("El programa no puede continuar, el archivo")

if __name__ == "__main__":
    main()
