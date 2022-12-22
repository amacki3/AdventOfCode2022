highestCalories = [0,0,0]
currentCalories = 0


with open('input.txt') as f:
    for line in f:
        strippedLine = line.strip('\n')
        if len(strippedLine) == 0:
            if currentCalories > highestCalories[0]:
                highestCalories[0] = currentCalories
                highestCalories.sort()
            currentCalories = 0
        else:
            currentCalories += float(strippedLine)

if currentCalories > highestCalories[0]:
    highestCalories[0] = currentCalories
print(sum(highestCalories))     

 
