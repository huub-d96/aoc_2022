""" Advent of Code Day 12

Hill climbing from A to Z

Author: Huub Donkers
Date: 12-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

#Templates for height and path map
height_map = [[-1]*len(data[0]) for _ in range(len(data))]
path_map = [[100000]*len(data[0]) for _ in range(len(data))]

#Fill height and path map
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell == 'S':
            height_map[i][j] = 0
            path_map[i][j] = 0
            start = [i,j,0,0,0]
        elif cell == 'E':
            height_map[i][j] = 26
            goal = [i,j,0,0,0]
        else:
            height_map[i][j] = ord(cell) - ord('a') #+ 1
            if height_map[i][j] == 0:
                path_map[i][j] = 0
            
#closed = [start[:2]]
closed = []
for i, row in enumerate(height_map):
    for j, cell in enumerate(row):
        if cell == 0:
            closed.append([i,j])
            
#Loop parameters   
length = 0
run = True        
adjacent = [[0,1], [1,0], [0,-1], [-1,0]]

#Flood map with distance values until endpoint is found
while(run):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):

            if path_map[i][j] == length:
                if [i,j] == goal[:2]:
    
                    run = False
                    path = [[i,j]]
                    path_length = length
                    for k in range(length):
                        for adj in adjacent:
                            child = [path[-1][0]+adj[0], path[-1][1]+adj[1]]
                                        
                            #Check if child in in boundaries
                            if child[0] > (len(path_map) - 1) or child[0] < 0 or child[1] > (len(path_map[0]) -1) or child[1] < 0:
                                continue

                            #Check if we can walk to child
                            if height_map[path[-1][0]][path[-1][1]]-height_map[child[0]][child[1]] > 1:
                                continue
                                                    
                            if path_map[path[-1][0]+adj[0]][path[-1][1]+adj[1]] == path_length -1:
                                path.append([path[-1][0]+adj[0], path[-1][1]+adj[1]])
                                path_length -= 1
                                break
                        
                for adj in adjacent:
                    child = [i+adj[0], j+adj[1]]
            
                    #Check if child in in boundaries
                    if child[0] > (len(path_map) - 1) or child[0] < 0 or child[1] > (len(path_map[0]) -1) or child[1] < 0:
                        continue
            
                    #Check if we can walk to child
                    diff = height_map[child[0]][child[1]] - height_map[i][j]
                    if diff > 1:
                        continue 

                    # Check if we already labeled this node
                    if child in closed:
                        continue

                    #Set new map value and append to closed list
                    path_map[child[0]][child[1]] = length + 1
                    closed.append(child)
                    
    length += 1

#Print solution                 
for i, p in enumerate(path_map):
    for j, pp in enumerate(p):
        if [i,j] in path:
            print(f'\033[93m{data[i][j]}', end="")
        elif data[i][j] == 'b':
            print(f'\033[94m{data[i][j]}', end="")
        else:
            print(f'\033[96m{data[i][j]}', end="")
    print("")

print("Shortest path length:", len(path)-3)


