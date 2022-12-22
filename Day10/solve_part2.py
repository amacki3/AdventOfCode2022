cumulativeSignal = 0
register = 1
cycleCount = 0

def draw():
    if (cycleCount) % 40 == 0:
        print('')
    if abs(register - (cycleCount%40)) <= 1:
        print('#',end='')
    else:
        print('.',end='')


with open('input.txt','r') as f:
    draw()
    for lines in f:
        tokens = lines.split()
        if tokens[0] == 'noop':
            cycleCount += 1
            draw()
        elif tokens[0] == 'addx':
            cycleCount += 1
            draw()
            cycleCount += 1
            register += int(tokens[1])
            draw()