import re
import math
import time

file = open('/home/jake/adventofcode/day5/inputtest.txt', 'r')
lines = file.readlines()

def genMapArr(start, end):
    arr = []
    for i in lines[start:end+1]:
        arr.append([ int(x) for x in i.split()])
    return arr

class SeedRange():
    def __init__(self, source):
        self.range = source[1]
        self.destination = []
        if source[0] != -1:
            self.add_destination(source[0])

    def update_range(self, range):
        self.range = range

    def add_destination(self, destination):
        self.destination.append(destination)

    def get_source(self):
        return self.destination[-1]
    
    def get_range(self):
        return self.range
    
    def split_seedrange(self, newRange):
        self.update_range(self.range - newRange)
        offshoot = SeedRange([-1, newRange])

        for i in self.destination:
            offshoot.add_destination(i+self.range)

        return offshoot

seeds = [ int(x) for x in lines[0].split(':')[1].split()]

seedranges = [ SeedRange(seeds[i:i+2]) for i in range(0, len(seeds), 2)]

maps = []
maps.append(genMapArr(3,4))
maps.append(genMapArr(7,9))
maps.append(genMapArr(12,15))
maps.append(genMapArr(18,19))
maps.append(genMapArr(22,24))
maps.append(genMapArr(27,28))
maps.append(genMapArr(31,32))

for mapp in maps:
    i = 0
    while i < len(seedranges):
        source = seedranges[i].get_source()
        rang = seedranges[i].get_range()
    
        destination = source

        for entry in mapp[::-1]:
            print(source)
            if entry[1] <= source and entry[1] + entry[2] - 1 >= source + rang - 1:
                seedranges[i].add_destination(entry[0] + source - entry[1])
            elif entry[1] <= source and entry[1] + entry[2] - 1 > source:
                seedranges.append(seedranges[i].split_seedrange(source + rang - entry[1] - entry[2]))
                rang = seedranges[i].get_range()
                seedranges[i].add_destination(entry[0] + source - entry[1])
            elif entry[1] > source and entry[1] < source + rang:
                seedranges.append(seedranges[i].split_seedrange(rang - entry[1] + source))
                rang = seedranges[i].get_range()
        
        if destination == source:
            seedranges[i].add_destination
        i += 1
    
print([ x.get_source() for x in seedranges ])
print(min([ x.get_source() for x in seedranges ] ) ) 