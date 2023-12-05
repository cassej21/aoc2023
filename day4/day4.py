import re
import math

file = open('/home/jake/adventofcode/day4/input.txt', 'r')
lines = file.readlines()

numbers = 0

cards = [1] * 197
card = 0

for i in lines:
    winning = i.split(':')[1].split('|')[0].split()
    my_nums = i.split(':')[1].split('|')[1].split()

    count = 0
    for j in winning:
        if j in my_nums:
            count += 1

    cur = 1
    while cur <= count and card + cur < 197:
        cards[card+cur] += cards[card]    
        cur += 1

    card += 1

print(sum(cards))

