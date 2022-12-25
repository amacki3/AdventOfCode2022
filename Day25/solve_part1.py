import numpy as np
totalValue = 0

charInterpret = {'=':-2,
                 '-':-1,
                 '0':0,
                 '1':1,
                 '2':2}

valueInterpret = {-2:'=',
                   -1:'-',
                   0:'0',
                   1:'1',
                   2:'2'}




with open('input.txt','r') as f:
    for line in f:
        line = line.strip()
        for power,char in enumerate(line):
            totalPower = len(line)-1
            value = (5**(totalPower-power))*charInterpret[char]
            totalValue += value

def convToSnafu(value):
    maxPower = np.floor(np.log10(value)/np.log10(5))
    if (5**maxPower) * 3 < value:
        maxPower = maxPower + 1
    if value > 5**maxPower:
        char = '2'
    else: 
        char = '1'
    enumValue = value - ((5**maxPower)*charInterpret[char])
    string = ''
    string = string + char
    while enumValue != 0:
        maxPower = maxPower - 1
        value = int(np.round((enumValue / (5**maxPower))))
        char = valueInterpret[value]
        string = string + char
        enumValue = enumValue - ((5**abs(maxPower)) * value)
    if maxPower != 0:
        string = string + '0'
        maxPower =- 1
    print(string)



convToSnafu(totalValue)

    
