cumulativeSignal = 0
register = 1
cycleCount = 0
with open('input.txt','r') as f:
    for lines in f:
        tokens = lines.split()
        if tokens[0] == 'noop':
            cycleCount += 1
            if (cycleCount-20) % 40 == 0:
                cumulativeSignal += register * cycleCount
                print(cumulativeSignal,register)
        elif tokens[0] == 'addx':
            cycleCount += 1
            if (cycleCount-20) % 40 == 0:
                cumulativeSignal += register * cycleCount
                print(cumulativeSignal,register)
           
            cycleCount += 1
            if (cycleCount-20) % 40 == 0:
                cumulativeSignal += register * cycleCount#
                print(cumulativeSignal,register)
            register += int(tokens[1])

print(cumulativeSignal)
