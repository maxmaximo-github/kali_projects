#!/usr/bin/env python3

from os import name
from os import Popen
from subprocess import run


if name != "nt":
    reply = Popen(["ping", "-c 3", "2001:db8:cafe::1"], capture_output=True)
    if reply == 0:

        print("El dispositivo es alcanzado por ping")
    else:
        print("Hola Mundo")

else:
    pass
