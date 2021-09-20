#!/usr/bin/env python3


def greet(name=None):

    return f"Hello, {name}"


def main():

    # name = "Datacamp"
    print(f"{greet()}")

if __name__ == '__main__':
    main()
