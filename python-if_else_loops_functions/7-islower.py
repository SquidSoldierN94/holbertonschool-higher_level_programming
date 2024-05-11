def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        print(f"{c} is lower")
    elif ord('A') <= ord(c) <= ord('Z'):
        print(f"{c} is upper")
    else:
        print("{}")
