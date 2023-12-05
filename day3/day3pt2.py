import re

file = open('/home/jake/adventofcode/day3/input.txt', 'r')
lines = file.readlines()

def adjacentSymbol(coords):
    for i in range(coords[0], coords[1]):
        for j in range(coords[2], coords[3]):
            if re.findall(r'[^\d\.\n]', lines[i][j]):
                return coords[4]

    return 0


numbers = 0 

line = 0
nums = []
for i in lines:
    x_min = max(line-1, 0)
    x_max = min(line+2, len(lines))

    for m in re.finditer(r'\d+', i):
        nums.append([x_min, x_max, max(m.start(0)-1, 0), min(m.end(0) + 1, len(i)), int(m.group(0)) ])
    line += 1

for i in nums:
    numbers += adjacentSymbol(i)

print(numbers)

