""" Advent of Code Day 2

Strategy to dominate elves in
rock-paper-scissors

Author: Huub Donkers
Date: 02-12-2022
"""

#Open input file
file = open('day2_input.txt', 'r')

#Maps
WL_map = [[3, 6, 0],
          [0, 3, 6],
          [6, 0, 3]]

#Read data 
data = [line.strip().split(" ") for line in file]

#Loop over moves
points = 0
for d in data:
    move_O = ord(d[0]) - ord('A') # Get index for opponets move

    # Part 1
    # move_M = ord(d[1]) - ord('X') # Get index for my move

    # Part 2
    outcome = 3*(ord(d[1]) - ord('X'))      # Get the outcome points
    move_M =  WL_map[move_O].index(outcome) # Find which my move based on outcome
    
    #Add move points
    points += move_M + 1

    #Add outcome points
    points += WL_map[move_O][move_M]
    
# Print results
print(points)
