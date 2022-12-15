""" Advent of Code Day 15

Exploring a cave!

Author: Huub Donkers
Date: 15-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

# Part 1
#Target row to check
y_target = 10

#Part 2
#Search and compare
search_min = 0
search_max = 4000000

#Build map
x_length = search_max
y_length = search_max
#cave_map = [[0]*y_length for _ in range(x_length)]
cave_map = {}
x_off = -10
y_off = -10

potentials = []
sensors = []
#Add sensors and beacons
for d in data:
    print(d)
    S_dat, B_dat = d.split(':')

    #Get sensor coordinates
    S_datx, S_daty = S_dat[10:].split(',')
    xS = int(S_datx.split("=")[1])
    yS = int(S_daty.split("=")[1])
    #if yS == y_target:
    #cave_map[xS-x_off][yS-y_off] = 'S'

    #Get beacon coordinates
    B_datx, B_daty = B_dat[23:].split(',')
    xB = int(B_datx.split("=")[1])
    yB = int(B_daty.split("=")[1])
    #if yB == y_target:
    #cave_map[xB-x_off][yB-y_off] = 'B'

    if True: #[8,7] == [xS, yS]:
        dist = abs(xS-xB)+abs(yS-yB)

        sensors.append([xS, yS, dist])

        try:
            cave_map[str(xS-x_off)+str(yS-y_off+dist+1)] += 1
        except KeyError:
            cave_map[str(xS-x_off)+str(yS-y_off+dist+1)] = 1

        for i in range(dist+2):
            x = xS-x_off-i
            y = yS-y_off+dist+1-i

            if x >= 0 and x <= search_max and y >= 0 and y <= search_max:
                try:
                    cave_map[str(x)+str(y)] += 1
                except KeyError:
                    cave_map[str(x)+str(y)] = 1

                if cave_map[str(x)+str(y)] == 4:
                    potentials.append([xS-i, yS+dist+1-i])

            x = xS-x_off+i
            y = yS-y_off+dist+1-i

            if x >= 0 and x <= search_max and y >= 0 and y <= search_max:            
                try:
                    cave_map[str(x)+str(y)] += 1 
                except KeyError:
                    cave_map[str(x)+str(y)] = 1 
                    
                if cave_map[str(x)+str(y)] == 4:
                    potentials.append([xS+i, yS+dist+1-i])   
            

        for i in range(dist+1):

            x = xS-x_off-i
            y = yS-y_off-(dist+1)+i
            if x >= 0 and x <= search_max and y >= 0 and y <= search_max:
                try:
                    cave_map[str(x)+str(y)] +=1
                except KeyError:
                    cave_map[str(x)+str(y)] = 1
                
                if cave_map[str(x)+str(y)] == 4:
                    potentials.append([xS-i, yS-(dist+1)+i])   

            x = xS-x_off+i
            y = yS-y_off-(dist+1)+i
            if x >= 0 and x <= search_max and y >= 0 and y <= search_max:
                try:
                    cave_map[str(x)+str(y)] +=1

                except KeyError:
                    cave_map[str(x)+str(y)] = 1

                if cave_map[str(x)+str(y)] == 4:
                    potentials.append([xS+i, yS-(dist+1)+i])       


'''Part 1
    #Add scanning area
    if True:
        dist = abs(xS-xB)+abs(yS-yB)
        
        if y_target >= yS and y_target < yS + dist:
            for i in range(dist-(y_target-yS)+1):
                if cave_map[xS-x_off+i][y_target-y_off] == '.':
                    cave_map[xS-x_off+i][y_target-y_off] = '#'
                if cave_map[xS-x_off-i][y_target-y_off] == '.':
                    cave_map[xS-x_off-i][y_target-y_off] = '#'

        if y_target <= yS and y_target > yS - dist:
            for i in range(dist+(y_target-yS)+1):
                if cave_map[xS-x_off+i][y_target-y_off] == '.':
                    cave_map[xS-x_off+i][y_target-y_off] = '#'
                if cave_map[xS-x_off-i][y_target-y_off] == '.':
                    cave_map[xS-x_off-i][y_target-y_off] = '#'
    '''

'''     
no_B_pos = 0           

for i in range(len(cave_map)):
    if cave_map[i][y_target-y_off] in ['#','S']:
        no_B_pos += 1 

print("")   
 
#Print map
for i in range(len(cave_map[0])):
   for j in range(len(cave_map)):
        print(cave_map[j][i], end="") #Transpose matrix for view
   print("")
    
print("No beacon positions:", no_B_pos)          
'''
#print(cave_map)
print(potentials)
print(sensors)


for pot in potentials:
    if pot[0] >= 0 and pot[0] <= search_max and pot[1] >= 0 and pot[1] <= search_max:
        in_range = False
        for sensor in sensors:    
            dist = abs(pot[0]-sensor[0])+abs(pot[1]-sensor[1])
            if sensor[2] >= dist:
                in_range = True

        if not in_range:
            print('Found!')
            distress = pot
            break
    

        
    
print("Found distress beacon at:", distress)            
print("Tuning frequency is:", distress[0]*4000000+distress[1])
    



