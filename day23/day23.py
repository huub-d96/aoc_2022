""" Advent of Code Day 23

Shouting monkeys

Author: Huub Donkers
Date: 23-12-2022
"""

def replace_coord(map_data, row, col, val):
    map_data[row] = map_data[row][:col] + val + map_data[row][col+1:]

def bound(low, high, value):
    return max(low, min(high, value))
#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

init_map = []

width = 240
height = 240
#Expand map
for _ in range((height-len(data))//2):
    init_map.append('.'*width)
for i in range(len(data)):
    init_map.append('.'*((width-len(data[i]))//2) + data[i] + '.'*((width-len(data[i]))//2 + (width-len(data[i]))%2))
for _ in range((height-len(data))//2 + (height-len(data))%2):
    init_map.append('.'*width)

for d in init_map:
    print(d)
print("")

#Rounds
move_round = 0
proposed = [1,1]

#for i in range(20):
i = -1
while proposed != []:
    i+= 1
    move_round += 1
    #Proposed moves
    proposed = []
    for row in range(len(init_map)):
        for col in range(len(init_map[0])):
            if init_map[row][col] == "#":

                north = init_map[bound(0,len(init_map)-1,row-1)][col-1:col+2] #if row-1 >= 0 else '#'
                south = init_map[bound(0,len(init_map)-1,row+1)][col-1:col+2] #if row+1 <= len(init_map) else '#'
                west = [init_map[r][bound(0,len(init_map[0])-1,col-1)] for r in range(bound(0,len(init_map),row-1),bound(0,len(init_map),row+2))] #if col+1 <= len(init_map[0]) else '#'
                east = [init_map[r][bound(0,len(init_map[0])-1,col+1)] for r in range(bound(0,len(init_map),row-1),bound(0,len(init_map),row+2))] #if col-1 >= 0 else '#'

                dirs = [north, south, west,east]
                props = [[row,col,row-1,col], [row,col,row+1,col], [row,col,row,col-1], [row,col,row,col+1] ]
                if '#' in [*north, *south, *west, *east]:
                
                    if '#' not in dirs[i%4]: #North
                        #print(init_map[row-1][col-1:col+2])
                        proposed.append(props[i%4])
                    elif '#' not in dirs[(i+1)%4]: #South
                        proposed.append(props[(i+1)%4])
                    elif '#' not in dirs[(i+2)%4]: #West
                        proposed.append(props[(i+2)%4])
                    elif '#' not in dirs[(i+3)%4]: #East
                        proposed.append(props[(i+3)%4])
                    else:
                        #print('???')
                        pass

    #Execute proposed moves
    for j, move in enumerate(proposed):
        conflict = False
        other_moves = proposed.copy()
        del other_moves[j]
        for move2 in other_moves:
            if move[2] == move2[2] and move[3] == move2[3]:
                conflict = True

        if not conflict:
            replace_coord(init_map, move[0], move[1],'.')
            replace_coord(init_map, move[2], move[3],'#')
            
    #print(proposed)

    
for d in init_map:
    print(d)
print("")

#Truncate map
for i in range(len(init_map)):
    if '#' in init_map[i]:
        upper = i
        break

for i in range(len(init_map)):
    if '#' in init_map[len(init_map)-1-i]:
        lower = len(init_map)-1-i
        break

for i in range(len(init_map[0])):
    for j in range(len(init_map)):
        if init_map[j][i] == "#":
            left = i
            break
    else:
        continue
    break

for i in range(len(init_map[0])):
    for j in range(len(init_map)):
        if init_map[j][len(init_map[0])-1-i] == "#":
            right = len(init_map[0])-1-i
            break
    else:
        continue
    break

print(upper,lower,left,right)
final_map = init_map[upper:lower+1]

for i in range(len(final_map)):
    final_map[i] = final_map[i][left:right+1]


for d in final_map:
    print(d)

empty = 0
for i in range(len(final_map)):
    for j in range(len(final_map[0])):
        if final_map[i][j] == '.':
            empty += 1

print("Empty tiles:", empty)
print("Rounds:", move_round)
