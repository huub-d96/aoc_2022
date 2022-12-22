""" Advent of Code Day 21

Shouting monkeys

Author: Huub Donkers
Date: 21-12-2022
"""
from collections import deque

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

'''
#Part 1
root = 0
i = 0
while root == 0:
    var, cmd = data[i%len(data)].split(":")

    try:
        #print(f'{var} ={cmd}')
        exec(f'{var} ={cmd}')
    except NameError:
        #print("Non-exist")
        #break
        pass

    i += 1

print(root)
'''

#Part 2
root = 0
i = 0
humn1 = 3678125408017
humn = humn1
while root == 0:
    var, cmd = data[i%len(data)].split(":")

    if var == 'root':
        v1, v2 = cmd.strip().split(" + ")

    if var == 'humn':
        i += 1
        continue

    try:
        #print(f'{var} ={cmd}')
        exec(f'{var} ={cmd}')
    except NameError:
        #print("Non-exist")
        #break
        pass

    i += 1

exec(f'r1 = {v1}')
exec(f'r2 = {v2}')

for d in data:
    var, cmd = d.split(":")

    #print("del", var)
    exec(f'del {var}')

root = 0
i = 0
humn2 = 54
humn = humn2
while root == 0:
    var, cmd = data[i%len(data)].split(":")

    if var == 'root':
        v1, v2 = cmd.strip().split(" + ")

    if var == 'humn':
        i += 1
        continue

    try:
        #print(f'{var} ={cmd}')
        exec(f'{var} ={cmd}')
    except NameError:
        #print("Non-exist")
        #break
        pass

    i += 1

exec(f'r3 = {v1}')
exec(f'r4 = {v2}')

print(r1,r3)
print(r2,r4)

if r2 == r4:
    d_root = r3-r1
    target = r2
    start = r1
else:
    d_root = r4-r2
    target = r1
    start = r2

d_humn = humn2 - humn1

dydx = d_root/d_humn

offset = start-dydx*humn1

#y=dydx*humn1+offset
humn_target = (target-offset)/dydx

print(humn_target)

