""" Advent of Code Day 3

Packing backs for elves. Finds the common letter 
between diffent sets of contents and prints the 
sum of their values

Author: Huub Donkers
Date: 03-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = file.readlines()

#Read data
points = 0
'''
# Part 1
for i in range(len(data)):

    # Define contents to compare
    contents = data[i].strip()
    half = int(len(contents)/2)
    cont1 = contents[0:half]
    cont2 = contents[half:]

    # Compare each letter in content 1 to content 2, sum the common letter
    for c in cont1:
        if c in cont2:          
            points += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
            break
    '''

# Part 2
for i in range(int(len(data)/3)):

    # Define contents to compare
    cont1 = data[3*i].strip()
    cont2 = data[3*i+1].strip()
    cont3 = data[3*i+2].strip()

    # Compare each letter in content 1 to content 2 and 3, sum the common letter
    for c in cont1:
        if c in cont2 and c in cont3:           
            points += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
            break    

print(points)

