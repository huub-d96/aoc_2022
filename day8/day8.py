""" Advent of Code Day 8

Hiding in the trees!

Author: Huub Donkers
Date: 08-12-2022
"""

#Function to rotate array 90 degrees clockwise
def rotate(array):    

    rows = len(array)
    cols = len(array[0])

    rot = [[0]*rows for _ in range(cols)]
    
    for x in range(rows):
        for y in range(cols):
            rot[y][rows - x - 1] = array[x][y]

    return rot

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]
hidden = [[0]*len(data[0]) for x in range(len(data))]
scenic = [[1]*len(data[0]) for x in range(len(data))]

#Find hidden trees
num_hidden = 0 
for side in range(4):
    for i, row in enumerate(data):
        lowest = -1
        for j, height in enumerate(row):
            if int(height) > lowest:
                lowest = int(height)
            else:
                hidden[i][j] += 1
                if hidden[i][j] == 4:
                    num_hidden += 1

    data = rotate(data)
    hidden = rotate(hidden)

# Find the tree with the best viewpoint
largest_view = 0
for side in range(4):
    for i, row in enumerate(scenic):
        for j, val in enumerate(row):
            seen = 0
            for k in range(j+1, len(row)):
                seen += 1
                if int(data[i][k]) >= int(data[i][j]):
                    break                

            scenic[i][j] *= seen 
            if scenic[i][j] > largest_view and side == 3:
                largest_view = scenic[i][j]
    data = rotate(data)
    scenic = rotate(scenic)
            
# Part 1
print("Number of hiding spots:", num_hidden)
print("Visible spots:", len(data)*len(data[0]) - num_hidden)

# Part 2
print("Best view score:", largest_view)
