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


for rucksack in fileContent:
    commonItem = findCommonItem(getFirstCompartment(rucksack), getSecondCompartment(rucksack))
    priorityScore += getPriorityScore(commonItem)

print(priorityScore)

