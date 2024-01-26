#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            uppercase = chr(ord(c)-32)
        else:
            uppercase = c
        print("{}".format(uppercase), end="")
    print()
