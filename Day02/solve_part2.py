ROCK = 0
PAPER = 1
SCISSORS = 2

LOSE = 0
DRAW = 3
WIN = 6

decodeDict = {
    'A' : ROCK,
    'B' : PAPER,
    'C' : SCISSORS,
    'X' : LOSE,
    'Y' : DRAW,
    'Z' : WIN
}

def getPointsFromChoice(first,second):
    first = decodeDict[first]
    if second == 'X':
        second = (first - 1) % 3
    elif second == 'Y':
        second = first
    else:
        second = (first + 1) % 3
    return second + 1


score = 0
with open("input.txt") as f:
    for line in f:
        vals = line.split()
        pts = getPointsFromChoice(vals[0],vals[1])
        score += pts + decodeDict[vals[1]]

print(score)