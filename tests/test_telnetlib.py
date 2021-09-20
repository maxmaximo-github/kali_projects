#!/usr/bin/env  python3


from telnetlib import Telnet
from socket import gaierror

telnet_server = "sw2.example.com"
try:
    with Telnet(host=f"{telnet_server}") as tel_con:

        tel_con.set_debuglevel(3)
        tel_con.read_until(bytes("Username: ", encoding="ascii"))
        tel_con.write(bytes("cesar\n", encoding="ascii"))

        tel_con.read_until(bytes("Password: ", encoding="ascii"))
        tel_con.write(bytes("cesar\n", encoding="ascii"))

        tel_con.read_all()



except ConnectionRefusedError:
    print("Conexion rechazada por el servidor.")

except ConnectionAbortedError:
    print("Conexion cerrada por el servidor.")


except (gaierror):
    print(f"No se puede resolver el nombre para {telnet_server}")
