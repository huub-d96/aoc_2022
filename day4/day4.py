""" Advent of Code Day 4

Packing backs for elves. How many sections
are fully contained within another section
and how many sections overlap?

Author: Huub Donkers
Date: 04-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = file.readlines()

#Read data
fully_contained = 0
overlapped = 0
for pair in data:
    s0, s1 = pair.strip().split(",") #Split data into first and second section
    b0, e0 = map(int, s0.split("-"))
    b1, e1 = map(int, s1.split("-"))

    #Check if small set is fully contained in larger set
    if e0-b0 >= e1-b1:
        if b1 >= b0 and e1 <= e0:
            fully_contained += 1
    else:
        if b0 >= b1 and e0 <= e1:
            fully_contained +=1

    #Check for overlap
    if e0-b0 >= e1-b1:
        section = range(b0, e0+1)
        if b1 in section or e1 in section:
            overlapped += 1
    else:
        section = range(b1, e1+1)
        if b0 in section or e0 in section:
            overlapped += 1
    
        
print(f"Fully contained: {fully_contained}")
print(f"Overlapped: {overlapped}")
