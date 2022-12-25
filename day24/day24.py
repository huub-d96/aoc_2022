""" Advent of Code Day 24

Blizzard evasion!

Author: Huub Donkers
Date: 24-12-2022
"""
'''
directions = {'^':[-1,0], '>':[0,1], 'v':[1,0], '<':[0,-1]}

def replace_coord(map_data, row, col, val):
    map_data[row] = map_data[row][:col] + str(val) + map_data[row][col+1:]

def move_blizzard(map_data, row, col, new_row, new_col, val):

    #Draw new coord
    if map_data[new_row][new_col] == '.':
        replace_coord(map_data, new_row, new_col, val)
    elif map_data[new_row][new_col] in directions.keys():
        replace_coord(map_data, new_row, new_col, 2)      
    
    else:
        replace_coord(map_data, new_row, new_col, int(map_data[new_row][new_col]) + 1)

        
    #Edit previous
    if map_data[row][col] in directions.keys():
        replace_coord(map_data, row, col, '.')
    elif int(map_data[row][col]) - 1 == 1:
        replace_coord(map_data, row, col, '9')
    else:
        replace_coord(map_data, row, col, int(map_data[row][col]) - 1)

#Add inital map to map array
maps = [data]

#Number of minutes
for _ in range(5):
    #Draw next state
    new_map = maps[-1].copy() #Use the previous map as input
    for row in range(len(data)):
        for col in range(len(data[0])):
            if maps[-1][row][col] in directions.keys():
            
                step = directions[maps[-1][row][col]]
                new_row = ((row+step[0] - 1) % (len(data) - 2)) + 1
                new_col = ((col+step[1] - 1) % (len(data[0]) - 2)) + 1
                
                move_blizzard(new_map, row, col, new_row, new_col, new_map[row][col])

            elif maps[-1][row][col] in ['1','2','3','4']:
                if maps[-2][row-1][col] == 'v':
                    step = directions['v']
                    new_row = ((row+step[0] - 1) % (len(data) - 2)) + 1
                    new_col = ((col+step[1] - 1) % (len(data[0]) - 2)) + 1
                    move_blizzard(new_map, row, col, new_row, new_col, 'v')
                    
                if maps[-2][row+1][col] == '^':
                    step = directions['^']
                    new_row = ((row+step[0] - 1) % (len(data) - 2)) + 1
                    new_col = ((col+step[1] - 1) % (len(data[0]) - 2)) + 1
                    move_blizzard(new_map, row, col, new_row, new_col, '^')

                if maps[-2][row][col-1] == '>':
                    step = directions['>']
                    new_row = ((row+step[0] - 1) % (len(data) - 2)) + 1
                    new_col = ((col+step[1] - 1) % (len(data[0]) - 2)) + 1
                    move_blizzard(new_map, row, col, new_row, new_col, '>')

                if maps[-2][row][col+1] == '<':
                    step = directions['<']
                    new_row = ((row+step[0] - 1) % (len(data) - 2)) + 1
                    new_col = ((col+step[1] - 1) % (len(data[0]) - 2)) + 1
                    move_blizzard(new_map, row, col, new_row, new_col, '<')


    maps.append(new_map)


#Print maps
for mp in maps:
    for row in mp:
        print(row)
    print("")
'''


#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

def replace_coord(map_data, row, col, val):
    map_data[row] = map_data[row][:col] + str(val) + map_data[row][col+1:]
    

#index all blizzards
blizzards = []
empty_map = data.copy()
directions = {'^':[-1,0], '>':[0,1], 'v':[1,0], '<':[0,-1]}
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] in directions.keys():
            blizzards.append([row,col, data[row][col]])
            replace_coord(empty_map, row, col, '.')
            


def gen_map(i):
    new_map = empty_map.copy()
    for blizzard in blizzards:
        step = directions[blizzard[2]]
        new_row = ((blizzard[0]+step[0]*i - 1) % (len(data) - 2)) + 1
        new_col = ((blizzard[1]+step[1]*i - 1) % (len(data[0]) - 2)) + 1

        if new_map[new_row][new_col] == '.':
            replace_coord(new_map, new_row, new_col, blizzard[2])
        elif new_map[new_row][new_col] in directions.keys():
            replace_coord(new_map, new_row, new_col, '$')# 2)
        else:
            replace_coord(new_map, new_row, new_col, '$') #int(new_map[new_row][new_col])+1)

    #Pad map
    new_map = ['#'*len(data[0])] + new_map + ['#'*len(data[0])]
    
    return new_map

#for i in range(4):
#    for row in gen_map(i):
#        print(row)
#    print("")


#Add new maps
it = 0
location = [1,1]
ends = [[len(data), len(data[0])-2], [1,1], [len(data), len(data[0])-2]]
end_it = 0

#Draw initial map:
maps = []
map0 = gen_map(0)
replace_coord(map0, location[0], location[1], 0)
maps.append(map0)


while end_it < 3:
    new_map = gen_map(it+1)
    skip = False
    for row in range(len(maps[it])):
        for col in range(len(maps[it][0])):
            if maps[it][row][col] not in ['^', '>', '<', 'v', '#', '.', '$']:

                if [row, col] == ends[end_it]:
                    print("Point", ends[end_it], "at", it, "minutes")
                    new_map = gen_map(it+1)
                    replace_coord(new_map, ends[end_it][0], ends[end_it][1], 0)
                    skip = True
                    end_it += 1

                if skip:
                    break
                    
                val = int(maps[it][row][col])

                #UP
                if new_map[row-1][col] == '.':
                    replace_coord(new_map, row-1, col, (val + 1)%10)
                elif new_map[row-1][col] not in ['^', '>', '<', 'v', '#', '$']:
                    replace_coord(new_map, row-1, col, (val + 1)%10)

                #DOWN
                if new_map[row+1][col] == '.':
                    replace_coord(new_map, row+1, col, (val + 1)%10)
                elif new_map[row+1][col] not in ['^', '>', '<', 'v', '#', '$']:
                    replace_coord(new_map, row+1, col, (val + 1)%10)

                #LEFT
                if new_map[row][col-1] == '.':
                    replace_coord(new_map, row, col-1, (val + 1)%10)
                elif new_map[row][col-1] not in ['^', '>', '<', 'v', '#', '$']:
                    replace_coord(new_map, row, col-1, (val + 1)%10)

                #RIGHT
                if new_map[row][col+1] == '.':
                    replace_coord(new_map, row, col+1, (val + 1)%10)
                elif new_map[row][col+1] not in ['^', '>', '<', 'v', '#', '$']:
                    replace_coord(new_map, row, col+1, (val + 1)%10)

                #WAIT
                if new_map[row][col] == '.':
                    replace_coord(new_map, row, col, (val + 1)%10)
                elif new_map[row][col] not in ['^', '>', '<', 'v', '#', '$']:
                     replace_coord(new_map, row, col, (val + 1)%10)

        if skip:
            break
    it+=1
    maps.append(new_map)


    
        

#for mp in maps:
#   for row in mp:
#        print(row)
#    print("")

print("Turns to find exit:", it-1)



