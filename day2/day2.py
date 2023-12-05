import re

file = open('/home/jake/adventofcode/day2/input.txt', 'r')
lines = file.readlines()

numbers = 0

setup = {
        'red': 12,
        'green': 13,
        'blue': 14
        }

setup = {}

game_num = 1
for i in lines:
    trials = i.split(':')[1].split(';')
    colors = [ trial.split(',') for trial in trials]

#    possible = True

    for trial in colors:
        for color in trial:
            num, col = color.split()[0], color.split()[1]
            if col not in setup.keys() or int(num) > setup[col]:
                setup[col] = int(num)

#    if possible:

    temp = 1

    for i in setup:
        temp = temp * setup[i]

    numbers += temp

    setup = {}

print(numbers)

