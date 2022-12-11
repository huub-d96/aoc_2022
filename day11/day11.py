""" Advent of Code Day 11

Monkey business

Author: Huub Donkers
Date: 11-12-2022
"""
import re

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]
sep = 7

#Get number of monkeys
num_monkeys = sum([d.startswith('Monkey') for d in data])

#Initial item array
items = []
dividers = []
common_multiple = 1
for i in range(num_monkeys):
    items.append(list(map(int, data[sep*i+1].split(':')[1].split(","))))
    common_multiple *= int(data[sep*i+3].split(" ")[-1])

#Initial inspections list
inspections = [0]*num_monkeys

rounds = 10000
for r in range(rounds):
    for m in range(num_monkeys):
        for i in range(len(items[m])):

            #New worry level
            old = items[m][i]
            operation = data[sep*m+2].split(":")[1].strip()
            exec(operation)
            items[m][i] = new % common_multiple #// 3

            #Throw to other monkey
            divider = int(data[sep*m+3].split(" ")[-1])
            if items[m][i] % divider == 0:
                to_m =  int(data[sep*m+4].split(" ")[-1])
            else:
                to_m =  int(data[sep*m+5].split(" ")[-1])

            items[to_m].append(items[m][i])

            #increment inspections
            inspections[m] +=1

        #Clear list of current monkey
        del items[m][:]
                

print(items)
print(inspections)
inspections.sort()
monkey_business_lvl = inspections[-1]*inspections[-2]

print("Monkey business level:", monkey_business_lvl)
#print(num_monkeys)
#print(data)
