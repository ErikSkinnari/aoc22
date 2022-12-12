itemCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorityScore = 0
fileContent = open("input.txt", "r")

def getFirstCompartment(rucksack):
    return rucksack[0:len(rucksack)//2]

def getSecondCompartment(rucksack):
    return rucksack[len(rucksack)//2:]

def getPriorityScore(item):
    return itemCollection.index(item) + 1

def findCommonItem(compartmentOne, compartmentTwo):
    return ''.join(set(compartmentOne).intersection(compartmentTwo))

def findBadgeItem(r1, r2, r3):
    return ''.join(set(r1).intersection(r2, r3, itemCollection))

# solution part 1
# for rucksack in fileContent:
#     commonItem = findCommonItem(getFirstCompartment(rucksack), getSecondCompartment(rucksack))
#     priorityScore += getPriorityScore(commonItem)

# solution part 2
rucksacks = []
for line in fileContent:
    rucksacks.append(line)

for index in range(0, len(rucksacks), 3):
    badge = findBadgeItem(rucksacks[index], rucksacks[index + 1], rucksacks[index + 2])
    priorityScore += getPriorityScore(badge)

print(priorityScore)
