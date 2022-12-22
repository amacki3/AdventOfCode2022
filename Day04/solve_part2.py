

total = 0

with open('input.txt','r') as f:
    for line in f:
        x = line.strip().split(',')
        vals = [[int(z) for z in y.split('-')] for  y in x]

        lowSet = set(range(vals[0][0],vals[0][1]+1))
        highSet = set(range(vals[1][0],vals[1][1]+1))

        common = lowSet.intersection(highSet)
        if len(common) > 0:
            total += 1
        

print(total)