""" Advent of Code Day 21

Shouting monkeys

Author: Huub Donkers
Date: 21-12-2022
"""
from collections import deque

#Open input file
file = open('input.txt', 'r')
data = [d.replace("\n","") for d in file.readlines()]

#Separate map and instructions
map_data = data[:-2].copy()
instructions = data[-1]

#Add instructions to list
path = []
current = ""
for i in range(len(instructions)):
    if instructions[i] in ['R', 'L']:
        path.append(current)
        path.append(instructions[i])
        current = ""
    else:
        current += instructions[i]

if instructions[-1] not in ['R', 'L']:
    path.append(current)
        
#Find start point
start_row = 0
start_col = map_data[start_row].index(".")

#Find sector starts
cube_size = 4
sector = []
row, col = 0,0
found_flag = False
while len(sector) < 6:
    try:
        if not found_flag:
            if not map_data[row][col] == " ":
                found_flag = True
                sector.append((row,col))
            
            col += cube_size
        else:
            if not map_data[row][col] == " ":
                found_flag = True
                sector.append((row,col))
            
            col += cube_size
    except:
        col = 0
        row += cube_size
        found_flag = False

print(sector)

def find_sector(row,col):
    sec_start_row = (row//cube_size)*cube_size
    sec_start_col = (col//cube_size)*cube_size

    return sector.index((sec_start_row, sec_start_col))  

def replace_coord(map_data, row, col, val):
    map_data[row] = map_data[row][:col] + val + map_data[row][col+1:]

def find_upper(map_data,row,col,direction):
    i = 0
    while True:
        try:
            if map_data[row+i*direction][col+i*(1-direction)] == " ":
                upper = ((row+i-1)*direction)%len(map_data) + ((col+i-1)*(1-direction))%len(map_data[row])
                break
        except:
            upper = ((row+i-1)*direction)%len(map_data) + ((col+i-1)*(1-direction))%len(map_data[row])
            break
        i += 1

    return upper

def find_lower(map_data,row,col,direction):
    i = 0
    while True:
        try:
            if map_data[row-i*direction][col-i*(1-direction)] == " ":
                lower = ((row-i+1)*direction)%len(map_data) + ((col-i+1)*(1-direction))%len(map_data[row])
                break
        except:
            lower = ((row-i+1)*direction)%len(map_data) + ((col-i+1)*(1-direction))%len(map_data[row])
            break
        i += 1

    return lower

replace_coord(map_data, start_row, start_col, ">")

directions = ((0,1),(1,0),(0,-1),(-1,0))
dir_icon = (">", "v", "<","^")
dir_it = 0
row, col = start_row, start_col

for p in path[:13]:
    
    if p == 'R':
        dir_it += 1
        replace_coord(map_data, row, col, dir_icon[dir_it%len(dir_icon)])
        continue

    elif p == 'L':
        dir_it -= 1
        replace_coord(map_data, row, col, dir_icon[dir_it%len(dir_icon)])
        continue

    for step in range(int(p)):

        col_upper = find_upper(map_data,row,col,False)
        col_lower = find_lower(map_data,row,col,False)
        row_upper = find_upper(map_data,row,col,True)
        row_lower = find_lower(map_data,row,col,True)

        new_row = row + directions[dir_it%len(directions)][0]
        new_col = col + directions[dir_it%len(directions)][1]

        current_sector = find_sector(row,col)

        sec_swap = [[[],[],[],[]],
                    [],
                    [],
                    [[],[2*cube_size,3*cube_size+row//cube_size+1,1],[],[]],
                    [[],[],[2*cube_size-1,cube_size-(row//cube_size+1),2],[]],
                    []]
        
        if new_row > row_upper: #Down exit
            print(current_sector)
            new_row = sec_swap[current_sector][2][0]
            new_col = sec_swap[current_sector][2][1]
            dir_it += sec_swap[current_sector][2][2]
        elif new_row < row_lower:
            new_row = row_upper
        elif new_col > col_upper: #Right exit          
            print(current_sector)
            new_row = sec_swap[current_sector][1][0]
            new_col = sec_swap[current_sector][1][1]
            dir_it += sec_swap[current_sector][1][2]
        elif new_col < col_lower:
            new_col = col_upper

        
        
        if map_data[new_row][new_col] == "#":
            break    
        else:
            row, col = new_row, new_col

        replace_coord(map_data, row, col, dir_icon[dir_it%len(dir_icon)])
        

for d in map_data:
    print(d)

#Compute password

print(row+1,col+1,dir_it%len(directions))

password = 1000*(row+1) + 4*(col+1) + dir_it%len(directions)

print("The password is:", password)

 
    
