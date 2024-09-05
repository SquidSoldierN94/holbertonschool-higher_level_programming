#!/usr/bin/python3
unique_sums = set()
for x in range(10):
    for i in range(10):
        unique_sums.add(x + i)
for number in unique_sums:
    print(number)
