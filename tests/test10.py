def pubkey_creation(device, data2):
    username, passphrase = data2
    # if not passphrase:
    #     passphrase = ascii_lowercase
    #     passphrase = "".join(choice(passphrase) for i in range(9))
    #     print(passphrase)
    home = Path.home()
    ssh_dir = Path(f"{home}/.ssh")


    if not Path(f"{ssh_dir}/{device}_id_rsa").is_file():
        if not passphrase:
            print("Aqui nos metemos o que onda")
            command = (
            f"ssh-keygen -f {ssh_dir}/{device}_id_rsa -b 4096 " +
            f"-C {username}@{device} -q").split()
            run(command, capture_output=True, input=b"\n")
        else:
            command = (
            f"ssh-keygen -f {ssh_dir}/{device}_id_rsa -b 4096 " +
            f"-C {username}@{device} -P {passphrase} -q").split()
            run(command, capture_output=True)


    else:
        path = Path(f"{ssh}/{device}_id_rsa")
        path.remove()
        command = (
        f"ssh-keygen -f {ssh_dir}/.ssh/{device}_id_rsa -b 4096 " +
        f"-C {username}@{device} -q -P {passphrase} -y").split()
        run(command, capture_output=True)
