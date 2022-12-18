""" Advent of Code Day 17

Rock stacking!

Author: Huub Donkers
Date: 17-12-2022
"""
import os, time

#Open input file
file = open('input.txt', 'r')
data = file.readlines()[0].strip()

rocks = [[[1,1,1,1],], 
         [[0,1,0],[1,1,1],[0,1,0]], 
         [[0,0,1], [0,0,1], [1,1,1]], 
         [[1],[1],[1],[1]], 
         [[1,1],[1,1]]]

def print_state(chamber, rock=[]):
    #os.system('clear')
    test_chamber = [r.copy() for r in chamber]

    if rock != []:
        for h in range(h_rock):
            for w in range(w_rock):
                test_chamber[row-h][col+w] += rock[h][w]

    for trow in reversed(test_chamber):
        print('|',end="")
        for cell in trow[1:-1]:
            print('#' if cell else '.', end="")
        print('|')
    print("")
    #print('+-------+')

    time.sleep(0.25)
            
#data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
#data = '<<<>>'
num_rocks = 10000
height = 0

gas_steps = len(data)

empty_row = [1, 0, 0, 0, 0, 0, 0, 0, 1]
chamber = [[1]*9, * [empty_row.copy() for _ in range(3)]]
gas_it = 0
prev_height = 0
steps = []
for n in range(num_rocks):
    #print(n/num_rocks)
    rock = rocks[n%len(rocks)]
    
    if isinstance(rock[0], list):
        h_rock = len(rock)
        w_rock = len(rock[0])
    else:
        h_rock = 1
        w_rock = len(rock)

    new_space = h_rock+3 - (len(chamber)-1-height)
    if new_space <0:
        new_space=0
    for _ in range(new_space):
        chamber.append(empty_row.copy())

    #Start position    
    row = h_rock + height + 3
    col = 3

    while True:
        #print(row)

        #print_state(chamber, rock)

        
        #Push left or right
        collision = False
        if data[gas_it%len(data)] == '<':
            direction = -1 
        elif data[gas_it%len(data)] == '>':
            direction = 1
        else:
            print("que?")
        #print(data[gas_it%len(data)])
        gas_it += 1
        for h in range(h_rock):
            for w in range(w_rock):
                #print(chamber[row-(1+h)][col+w], rock[h][w])
                if chamber[row-(h)][col+w+direction] + rock[h][w] > 1:
                    collision = True

        if not collision:
            col += direction

        #print_state(chamber, rock)
        
        #Fall one block
        collision = False
        for h in range(h_rock):
            for w in range(w_rock):
                #print(chamber[row-(1+h)][col+w], rock[h][w])
                if chamber[row-(1+h)][col+w] + rock[h][w] > 1:
                    collision = True

        if not collision:
            row -=1
        else:
            break

    #Draw
    for h in range(h_rock):
        for w in range(w_rock):
            chamber[row-h][col+w] += rock[h][w]

            if chamber[row-h][col+w] == 1 and row-h > height:
                height = row-h

#print(height)

    #Check for cycles
    
    if n != 0:
        #print_state(chamber[prev_height+1:height+1])
        steps.append([chamber[prev_height+1:height+1].copy(), height, gas_it])
        prev_height = height
    

for i, fit in enumerate(steps):
    
    match_flag = False
    for j, step in enumerate(steps):
        #print_state(step[0])
        if fit[0] == step[0] and i != j and (fit[2] - step[2]) % gas_steps == 0:
            #print("Found match!", i, j)
            match_flag = True
            break

    if match_flag:
        break
    
cycle_height = steps[j-1][1] - steps[i-1][1]
cycle_steps = j-i
height_before_cycle = steps[i-1][1]

rock_sims = 1000000000000

total_steps = rock_sims

total_heigth = cycle_height*((total_steps-i)//cycle_steps) + height_before_cycle
rem = (total_steps-i)%cycle_steps

total_heigth += steps[i-1+rem][1]-height_before_cycle-1

print(f'Total height after {rock_sims} rocks: {total_heigth}')

'''    
#Print the final rock tower
for row in reversed(chamber[1:]):
    print('|',end="")
    for cell in row[1:-1]:
        print('#' if cell else '.', end="")
    print('|')
print('+-------+')


print("height:", height)
'''
