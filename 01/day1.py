fileContent = open("input.txt", "r")

elves = []

elveCalorieCollection = 0

for line in fileContent:

    if line == "\n":
        elves.append(elveCalorieCollection)
        elveCalorieCollection = 0
    else:
        elveCalorieCollection = elveCalorieCollection + int(line)


# print(max(elves)) ## Part I

elves.sort(reverse = True)

topCalories = elves[0:3]
combinedCalories = sum(topCalories)
print(combinedCalories)

