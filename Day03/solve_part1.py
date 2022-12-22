
import math

total = 0
with open("input.txt",'r') as f:
    for line in f:
        line = line.strip()
        midpoint = float(len(line))/2.0

        first = set(line[0:math.floor(midpoint)])
        second = set(line[math.floor(midpoint):])
        common = first.intersection(second)
        common = common.pop()

        value = (ord(common.upper()) - 64) + ((ord(common) < 95) * 26)

        total += value

print(total)
