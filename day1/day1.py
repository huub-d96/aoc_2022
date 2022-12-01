""" Advent of Code Day 1

Finding calories! Reads calories per elf from
and input text file. Each elf carries a different
amout of foods with certain calories with him. Elves
are distinguised by a linebreak in the input file.

Author: Huub Donkers
Date: 01-12-2022
"""

#Open input file
file = open('day1_input.txt', 'r')

#Read data 
elf_cals = [0]
current_elf = 0

for line in file:
    if line != "\n":
        elf_cals[current_elf] += int(line)
    else:
        elf_cals.append(0)
        current_elf += 1

#Sort in descending order
elf_cals.sort(reverse=True)

#Get top 3
n = 3
top = sum([elf_cals[i] for i in range(n)])

#Print results
print(f"Calories top {n}: {top}")
