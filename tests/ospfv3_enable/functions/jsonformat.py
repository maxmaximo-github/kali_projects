#!/usr/bin/env python3


from json import load
from json import dumps
from json import JSONDecodeError
from os import getcwd
from pathlib import Path
from pathlib import PurePath


def JSONDataImport():

    try:
        file = Path(f"{PurePath()}/data/devices.json")
        # file = f"{getcwd()}/data/devices.json"
        # print(file)

        with file.open(mode="r") as f:
            data_json = load(f)
        # with open(file=file, mode="r") as f:
        #     data_json = load(f)

        # print(dumps(data_json, indent=4))

        return data_json

    except JSONDecodeError as error:
        print(f"El archivo {file} contiene errores.")
        print(error)
        return False
