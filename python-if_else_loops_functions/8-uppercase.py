#!/usr/bin/python3
def uppercase(str):
    uppercase_text = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_text += chr(ord(char) - 32)
        else:
            uppercase_text += char
    print(uppercase_text)
