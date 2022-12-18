""" Advent of Code Day 118

Rock stacking!

Author: Huub Donkers
Date: 17-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

surface_area = 0

xmax = ymax = zmax = 0

#Find dimensions
for cube in data:

    x,y,z = list(map(int,cube.split(',')))

    if x > xmax:
        xmax = x
    if y > ymax:
        ymax = y
    if z > zmax:
        zmax = z

model = [[[0]*zmax for y in range(ymax)] for x in range(xmax)]

#Build model
for cube in data:
    x,y,z = list(map(int,cube.split(',')))
    model[x-1][y-1][z-1] = 1
    
#print(model)   
air = []

#Find in air pockets that are not obscured
for x in range(xmax):
    for y in range(ymax):
        for z in range (zmax):
            in_sight = False
            
            # Look in x+ direction
            x_p_free = True
            for x_p in range(xmax-x-1):                
                if model[x+x_p+1][y][z] == 1:
                    x_p_free = False

            # Look in x- direction
            x_n_free = True
            for x_n in range(x):                
                if model[x-x_n-1][y][z] == 1:
                    x_n_free = False

            # Look in y+ direction
            y_p_free = True
            for y_p in range(ymax-y-1):                
                if model[x][y+y_p+1][z] == 1:
                    y_p_free = False

            # Look in y- direction
            y_n_free = True
            for y_n in range(y):                
                if model[x][y-y_n-1][z] == 1:
                    y_n_free = False

             # Look in z+ direction
            z_p_free = True
            for z_p in range(zmax-z-1):                
                if model[x][y][z+z_p+1] == 1:
                    z_p_free = False

            # Look in y- direction
            z_n_free = True
            for z_n in range(z):                
                if model[x][y][z-z_n-1] == 1:
                    z_n_free = False

            free = x_p_free + x_n_free + y_p_free + y_n_free + z_p_free + z_n_free
            is_cube = True if f'{x+1},{y+1},{z+1}' in data else False
            #is_air = True if f'{x+1},{y+1},{z+1}' in air else False
            if free > 0 and not is_cube:
                #print(x+1,y+1,z+1)
                air.append(f'{x+1},{y+1},{z+1}')
                pass

#Find air pockets that are connected to other air pockets
old_len = len(air)   
while True:
    for x in range(xmax):
        for y in range(ymax):
            for z in range (zmax):

                if f'{x+1},{y+1},{z+1}' not in data and f'{x+1},{y+1},{z+1}' not in air:
                    #print(x+1,y+1,z+1)

                    touch_air = False
                    if f'{x},{y+1},{z+1}' in air:
                        touch_air = True
            
                    if f'{x+2},{y+1},{z+1}' in air:
                        touch_air = True
                        
                    if f'{x+1},{y},{z+1}' in air:
                        touch_air = True
                        
                    if f'{x+1},{y+2},{z+1}' in air:
                        touch_air = True
                        
                    if f'{x+1},{y+1},{z}' in air:
                        touch_air = True
                        
                    if f'{x+1},{y+1},{z+2}' in air:
                        touch_air = True
                        

                    if touch_air:
                        #print(x+1,y+1,z+1)
                        air.append(f'{x+1},{y+1},{z+1}')

    if len(air) == old_len:
        break

    old_len = len(air)

#Find pockets that are not connected to air pockets and fill them as if they were cubes
for x in range(xmax):
    for y in range(ymax):
        for z in range (zmax):

            if f'{x+1},{y+1},{z+1}' not in data and f'{x+1},{y+1},{z+1}' not in air:
                #print(x+1,y+1,z+1)

                touch_air = False
                if f'{x},{y+1},{z+1}' in air:
                    touch_air = True
                    
                if f'{x+2},{y+1},{z+1}' in air:
                    touch_air = True
                    
                if f'{x+1},{y},{z+1}' in air:
                    touch_air = True
                    
                if f'{x+1},{y+2},{z+1}' in air:
                    touch_air = True
                    
                if f'{x+1},{y+1},{z}' in air:
                    touch_air = True
                    
                if f'{x+1},{y+1},{z+2}' in air:
                    touch_air = True
                    

                if not touch_air:
                    #print(x+1,y+1,z+1)
                    data.append(f'{x+1},{y+1},{z+1}')

# Compute surface area of cube  
for cube in data:

    x,y,z = list(map(int,cube.split(',')))
    
    neighbours = 0
    for neighbour in data: 
        xn,yn,zn = list(map(int,neighbour.split(',')))
        #print(x,y,z, xn,yn,zn)
        if xn == x+1 and y == yn and z == zn:
            neighbours +=1
        if xn == x-1 and y == yn and z == zn:
            neighbours +=1
        if xn == x and y+1 == yn and z == zn:
            neighbours +=1
        if xn == x and y-1 == yn and z == zn:
            neighbours +=1
        if xn == x and y == yn and z+1 == zn:
            neighbours +=1
        if xn == x and y == yn and z-1 == zn:
            neighbours +=1

    #print(neighbours)

    surface_area += 6 - neighbours

#Possible air pockets
#print(xmax, ymax, zmax)
print("Total surface area:", surface_area)


#2070 Too low
#2100 Too high

        
