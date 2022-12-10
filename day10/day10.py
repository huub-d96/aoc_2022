""" Advent of Code Day 10

CPU simulation

Author: Huub Donkers
Date: 10-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

#Global variables
X = 1
counter = 0
signal_sum = 0
checkpoints = [20, 60, 100, 140, 180, 220]

#Array to store CRT values
CRT = [['.']*40 for _ in range(6)]

#Draw pixel on CRT
def draw_pixel(counter, X):
    global CRT
    row = counter // 40
    col = counter % 40
    if col in range(X-1, X+2):
        CRT[row][col] = '#'

#Increment counter and check for checkpoints
def inc_and_check(value=0):
    global counter, X, signal_sum

    #Draw a pixel for current cycle
    draw_pixel(counter, X)

    #increment counter and check
    counter += 1
    if counter in checkpoints:
        signal_sum += X*counter

    #Add value to register X
    X += value

#Loop over all instructions    
for instruction in data:

    if instruction == "noop":
        inc_and_check()
    else:
        cmd, value = instruction.split(" ")
        inc_and_check()
        inc_and_check(int(value))

#Print results (Part 1)
print("Cycles:", counter)
print("X:", X)
print("Signal strength:", signal_sum)

#Print CRT (Part 2)
for row in CRT:
    print(*row)
