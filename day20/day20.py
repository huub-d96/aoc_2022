""" Advent of Code Day 20

Decrypting elves!

Author: Huub Donkers
Date: 20-12-2022
"""
from collections import deque

#Open input file
file = open('input.txt', 'r')
key = 811589153
data = [(i, int(d.strip())) for i, d in enumerate(file.readlines())]

output = deque(data.copy())
for _ in range(10):  
    for i,n in data:

        if n == 0:
            id0 = i
            continue

        idx = output.index((i,n))   

        output.remove((i,n))
        output.rotate(-n*key)
        output.insert(idx, (i,n))

   
idx_0 = output.index((id0,0))

n1 = output[(idx_0 + 1000) % (len(data))][1]*key
n2 = output[(idx_0 + 2000) % (len(data))][1]*key
n3 = output[(idx_0 + 3000) % (len(data))][1]*key

print(output)
print(n1, n2, n3)
print("Sum:", n1+n2+n3)


