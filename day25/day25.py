""" Advent of Code Day 25

Number conversions

Author: Huub Donkers
Date: 25-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]

snafu = {"=":-2, '-':-1, '0':0, '1': 1, '2':2}

def snafu_to_dec(number):
    dec = 0
    for i, num in enumerate(number):
        dec += snafu[num]*(5**(len(number)-i-1))
    return dec

def dec_to_snafu(n):

    lead = ''
    while n != 0:
        
        remainder = ((n+2) % 5) - 2
        n = n // 5

        if remainder < 0:
            n += 1

        lead = list(snafu.keys())[list(snafu.values()).index(remainder)] + lead
        
    return lead

snafu_sum = 0
for d in data:
    dec = snafu_to_dec(d)

    snafu_sum += dec

result = dec_to_snafu(snafu_sum)
print("SUM:", snafu_sum)
print('SNAFU SUM:', result)

