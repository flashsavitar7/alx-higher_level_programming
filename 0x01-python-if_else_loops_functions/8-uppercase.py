#!/usr/bin/python3
def uppercase(str_data):
    for char in str_data:
        if ord(char) >= 65:
            str_data += chr(ord(char) - 32)
    return str_data