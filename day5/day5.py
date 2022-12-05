""" Advent of Code Day 5

Stacking containers! Implementations of the 
CrateMover 9000 and 9001 models

Author: Huub Donkers
Date: 05-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = file.readlines()

#Create initial container array
containers = [['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
              ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
              ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
              ['R', 'S', 'C', 'L'],
              ['M', 'V', 'T', 'P', 'F', 'B'],
              ['T', 'R', 'Q', 'N', 'C'],
              ['G', 'V', 'R'],
              ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
              ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']]

#Execute all crane instructions
for instruction in data:

    #Get data for instruction string
    rep, start, end = list(map(int,instruction.strip().split(" ")[1::2]))

    '''
    #CrateMover 9000
    for i in range(rep):
        move = containers[start-1].pop()
        containers[end-1].append(move)
    '''
    
    #CrateMover 9001
    move = containers[start-1][-rep:]
    del containers[start-1][-rep:]
    containers[end-1] = containers[end-1] + move

#Check which containers are on top
output = ''
for i in range(len(containers)):
    output += containers[i][-1]

#Print output string
print(output)
