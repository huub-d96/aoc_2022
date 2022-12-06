""" Advent of Code Day 6

Finding unique substrings in 
very large strings!

Author: Huub Donkers
Date: 06-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = file.readlines()[0]

window_size = 14 

mark = window_size
while(1):
    lst = data[mark-window_size:mark]
    st = set(lst)
    if len(lst) == len(st):
        break

    mark += 1

print(mark)
