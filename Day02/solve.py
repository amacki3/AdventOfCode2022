ROCK = 0
PAPER = 1
SCISSORS = 2

decodeDict = {
    'A' : ROCK,
    'B' : PAPER,
    'C' : SCISSORS,
    'X' : ROCK,
    'Y' : PAPER,
    'Z' : SCISSORS
}


def getWinner(first,second):
    first = decodeDict[first]
    second = decodeDict[second]

    difference = second-first
    if difference == 0:
        return 1
    else:
        if abs(difference) > 1:
            return 0 if difference > 0 else 2
        else:
            return 2 if difference > 0 else 0
        


score = 0
with open("input.txt") as f:
    for line in f:
        vals = line.split()
        score += getWinner(vals[0],vals[1])*3 + (decodeDict[vals[1]]+1)

print(score)