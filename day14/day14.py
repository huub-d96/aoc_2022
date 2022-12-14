""" Advent of Code Day 14

Comparing lists of lists of lists

Author: Huub Donkers
Date: 14-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

#Build path
x_length = 400
rock_map = [['.']*170 for _ in range(x_length)]
x_off = 500 - x_length//2
y_off = 0

#x_length = 30
#rock_map = [['.']*12 for _ in range(x_length)]
#x_off = 500 - x_length//2
#y_off = 0

#Add start point
start = [500,0]
rock_map[start[0]-x_off][start[1]-y_off] = '+'


#Add rocks
lowest_point = 0
for path in data:
    coords = path.split(" -> ")

    xs, ys = list(map(int, coords[0].split(",")))
    if ys > lowest_point:
        lowest_point = ys
    for coord in coords[1:]:
        x, y = list(map(int, coord.split(",")))
        dx = x - xs
        dy = y - ys

        if y > lowest_point:
                lowest_point = y

        if dx == 0: #Move in y direction
            if dy > 0: #Move up
                for step in range(dy+1):
                    rock_map[xs-x_off][ys+step-y_off] = '#'
            else: # Move down
                for step in range(abs(dy)+1):
                    rock_map[xs-x_off][ys-step-y_off] = '#'
        elif dy == 0: #Move in y direction
            if dx > 0: #Move right
                for step in range(dx+1):
                    rock_map[xs+step-x_off][ys-y_off] = '#'
            else: # Move left
                for step in range(abs(dx)+1):
                    rock_map[xs-step-x_off][ys-y_off] = '#'

        #Update start point for next coord
        xs = x
        ys = y

#Add floor
for i in range(len(rock_map)):
    rock_map[i][lowest_point+2] = "#"

#Add sand
print(lowest_point)
run_sim = True
grains = 0
while run_sim:
    #Start point of sand
    x, y = start

    #Simulate fall
    while True:
        
        #print(x,y)
        #Check if we can fall down (actually up, as y increases when falling)
        if rock_map[x-x_off][y-y_off+1] == '.': 
            y += 1 #Step one down
        #Check if we can fall down left diagonally
        elif rock_map[x-x_off-1][y-y_off+1] == '.': 
            x -= 1
            y += 1
        #Check if we can fall down right diagonally
        elif rock_map[x-x_off+1][y-y_off+1] == '.': 
            x += 1
            y += 1
        else: #Rest
            rock_map[x-x_off][y-y_off] = 'o'
            grains += 1
            break

        #Part 1
        #if y == lowest_point:
        #    run_sim = False
        #    break

    #Part 2
    if [x,y] == start:
        run_sim = False
        break

                

#Print map
for i in range(len(rock_map[0])):
    for j in range(len(rock_map)):
        print(rock_map[j][i],"", end="") #Transpose matrix for view
    print("")
    
print("Number of grains at rest:", grains)
