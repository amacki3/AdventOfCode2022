highestCalories = 0
currentCalories = 0

with open('input.txt') as f:
    for line in f:
        strippedLine = line.strip('\n')
        if len(strippedLine) == 0:
            if currentCalories > highestCalories:
                highestCalories = currentCalories
            currentCalories = 0
        else:
            currentCalories += float(strippedLine)

if currentCalories > highestCalories:
    highestCalories = currentCalories
print(highestCalories)

 
