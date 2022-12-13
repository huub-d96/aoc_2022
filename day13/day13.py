""" Advent of Code Day 13

Comparing lists of lists of lists

Author: Huub Donkers
Date: 13-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]


#Function to compare two lists
def compare(left, right):

    #If both instances are ints, compare which one is bigger
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("Left smaller than right: Right order")
            return 1
        elif left > right:
            print("Right smaller than right: Wrong order")
            return -1
        else:
            return 0

    #If both are lists, compare their contencts recursively
    elif isinstance(left, list) and isinstance(right, list):
        shortest = left if len(left) < len(right) else right
        for i in range(len(shortest)):
            result = compare(left[i], right[i])
            if result == 1:
                return 1
            elif result == -1:
                return -1

        if len(left) < len(right):
            print("Left ran out of items: Right order")
            return 1
        elif len(left) > len(right):
            print("Right ran out of items: Wrong order")
            return -1
        else:
            return 0

    #If right instance is an in, format to list and compare again
    elif isinstance(left, list) and isinstance(right, int):
        result = compare(left, [right])
        return result

    #If left instance is an in, format to list and compare again
    elif isinstance(left, int) and isinstance(right, list):
        result = compare([left], right)
        return result

           
#Format data and add divider packets
divider_packets = [[[2]], [[6]]]
for i in range((len(data)+1)//3-1):
    data.remove("")

list_data = []
for item in data:
    exec("lst= "+item)
    list_data.append(lst)

list_data.extend(divider_packets)

#Sort packets inefficiently (swap two adjacnent packets if they are not in order)
while(True):

    sorted_packets = True
    for i in range(len(list_data)-1):
        result = compare(list_data[i], list_data[i+1])
        output = True if result == 1 else (False if result == -1 else "???")
        
        if not output:
            sorted_packets = False
            temp = list_data[i]
            list_data[i] = list_data[i+1]
            list_data[i+1] = temp

    if sorted_packets:
        break

#Find divider packets
pack_ID0 = list_data.index(divider_packets[0])+1
pack_ID1 = list_data.index(divider_packets[1])+1

#Print result
print("Decoder Key:", pack_ID0*pack_ID1)
        
        



