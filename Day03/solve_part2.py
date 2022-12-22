
import math

elves = [set(),set(),set()]

total = 0
with open("input.txt",'r') as f:
    for i,line in enumerate(f):
      
        line = line.strip()
        elves[i%3] = set(line)

        if (i+1) % 3 == 0:
            common = set.intersection(*elves)
            common = common.pop()
            value = (ord(common.upper()) - 64) + ((ord(common) < 95) * 26)

            total += value



print(total)
