#!/usr/bin/python3
# -*- coding: utf-8 -*-
import beer


def main():
    b = beer.Beer

    # Load beer from file and display deserialized string.
    # Note: You have to use UTF-8 encoding because of the special characters!
    with open("some_beer.txt", 'r', encoding='utf8') as file:
        print(b.deserialize_beer(file.read()), "\n")

    # Brew some beer
    print(b.serialize_beer("Wow such beer, very long."))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
