""" Advent of Code Day 7

Finding unique substrings in 
very large strings!

Author: Huub Donkers
Date: 07-12-2022
"""

#Function to add items to filesystem based on cli output
def add_item(path, file_stm, key, value):
   
    if len(path) == 0:
        if value == "dir":
            file_stm[key] = {"size": 0}
        else:
            file_stm[key] = int(value)
        
        return file_stm
    else:    
        current_dir = path[0]

        if current_dir not in file_stm:
            file_stm[current_dir] = add_item(path[1:], {"size": 0}, key, value)
        else:
            file_stm[current_dir] = add_item(path[1:], file_stm[current_dir], key, value)
               
        return file_stm   

#Recursive function that exlpores the filesystem and sums sizes of files and subdirs
def compute_sizes(file_stm):

    sums = 0
    for key in file_stm:

        if key == "size":
            copy = file_stm.copy()
            del copy['size']
            file_stm['size'] += compute_sizes(copy)
            return file_stm['size']
            
        elif isinstance(file_stm[key], int):
            sums += file_stm[key]
        else: 
            sums += compute_sizes(file_stm[key])
            
    return sums    

#Find the sum of the dirs under a thershold value
def sum_large_dirs(threshold, file_stm):
    sums = 0

    for key in file_stm:
        if key == "size" and file_stm[key] < threshold:
            sums += file_stm[key]
        elif not isinstance(file_stm[key], int):
            sums += sum_large_dirs(threshold, file_stm[key])

    return sums

#Find the small directory size that is large enough to free up space          
def find_smallest_deleteable(threshold, file_stm, cur_smallest = 1e10):    

    smallest = cur_smallest
    for key in file_stm:
        if key == "size" and file_stm[key] > threshold and file_stm[key] < smallest:
            smallest = file_stm[key]
        elif not isinstance(file_stm[key], int):
            smallest = find_smallest_deleteable(threshold, file_stm[key], smallest)  
            
    return smallest

#Open input file
file = open('input.txt', 'r')
data = file.readlines()

#Start with empty filesystem and root path
filesystem  = {}
path: list[str] = ['/']   

#Build the filesystem tree    
for cli in data:
    input = cli.strip().split(" ")

    #Process command
    if input[0] == "$":
        match input[1]:
            case "cd":
                match input[2]:
                    case "/":
                        path = ['/']
                    case "..":
                        path.pop()
                    case other:
                        path.append(input[2])

    #Process output
    else:
        add_item(path, filesystem, input[1], input[0])

#Compute sizes of each subdirs        
compute_sizes(filesystem["/"])

#Solution part 1
print("Sum of at most 100000 sized dirs:", sum_large_dirs(100000, filesystem["/"]))

#Solution part 2
total_disk_space = 70000000
used_space = filesystem["/"]['size']
available = total_disk_space - used_space
free_up = 30000000 - available

print("Used disk space:", used_space)
print("Available disk space:", available)
print("Extra space needed:", free_up)
print("Size of smallest deleteable dir:", find_smallest_deleteable(free_up, filesystem["/"]))
