

total = 0

with open('input.txt','r') as f:
    for line in f:
        x = line.strip().split(',')
        vals = [[int(z) for z in y.split('-')] for  y in x]
        if vals[0][0] < vals[1][0]:
            total += vals[0][1] >= vals[1][1]
        elif vals[0][0] == vals[1][0]:
            total += 1
        else:
            total += vals[1][1] >= vals[0][1]
        

print(total)