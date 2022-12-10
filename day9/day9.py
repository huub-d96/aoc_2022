""" Advent of Code Day 9

Usually the simplest approach works
best!

Author: Huub Donkers
Date: 09-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

#Init rope array
rope_length=10
rope = [[[1000,1000]] for _ in range(rope_length)] #Start coordinates of the rope [x,y]

#Fuction to move head 1 step based on input argument
def move_head(direction):

    x = y = 0
    match direction:
        case "R":
            x += 1
        case "L":
            x -= 1
        case "U":
            y += 1
        case "D":
            y -= 1
        case other:
            print("???") 
                 
    rope[0].append([rope[0][-1][0]+x, rope[0][-1][1]+y]) 

for move in data:

    #Cleanup data
    direction, distance = move.split(" ")
    distance = int(distance)

    #Do simulation step by step
    for step in range(distance):

        #Move rope head
        move_head(direction)        

        #Move rope links
        for i in range(1, rope_length):

            #Find x and y difference between current and previous link
            dx = rope[i-1][-1][0]-rope[i][-1][0]
            dy = rope[i-1][-1][1]-rope[i][-1][1]
            if abs(dx) > 1 or abs(dy) > 1:

                #Move rope in steps of 1 sideways or diagonal
                x = 1 if dx > 0 else (-1 if dx < 0 else 0)
                y = 1 if dy > 0 else (-1 if dy < 0 else 0)
                rope[i].append([rope[i][-1][0]+x, rope[i][-1][1]+y])

            
        
#Print output
T_str = [str(x)+str(y) for x,y in rope[-1]]
print("Tail steps:", len(rope[-1]))
print("Tail unique:", len(set(T_str)))
