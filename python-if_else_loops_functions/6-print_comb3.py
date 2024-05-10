#!/usr/bin/python3
result = ""
for i in range(10):
    for j in range(i + 1, 10):
        result += "{:02d}, ".format(i * 10 + j)

print(result[:-2])
