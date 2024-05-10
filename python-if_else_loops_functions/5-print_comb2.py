#!/usr/bin/python3
for x in range(00, 99):
    y = "{:02d}".format(x)
    print(f"{y}", end=', ')
else:
    print("99")
