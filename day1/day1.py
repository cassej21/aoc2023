import re

def text2int(s):
   
    words_to_numbers = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
    }
 
    pattern = re.compile(r'(' + '|'.join(words_to_numbers.keys()) + ')')
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], re.sub(pattern, lambda x: words_to_numbers[x.group()], s))

file = open('/home/jake/adventofcode/day1/input.txt', 'r')
lines = file.readlines()

numbers = [ int(re.findall('\d',text2int(x))[0] + re.findall('\d',text2int(x))[-1]) for x in lines]

print(sum(numbers))

