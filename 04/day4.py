input = open("input.txt", "r")

completeContainsCounter = 0

def rangeIsContained(range1x, range1y, range2x, range2y):
    if ((range1x <= range2x and range1y >= range2y) 
            or (range2x <= range1x and range2y >= range1y)):
        return True
    return False


for line in input:

    range1 = line.split(',')[0]
    range2 = line.split(',')[1]

    range1x = int(range1.split('-')[0])
    range1y = int(range1.split('-')[1])
    range2x = int(range2.split('-')[0])
    range2y = int(range2.split('-')[1])

    if rangeIsContained(range1x, range1y, range2x, range2y):
        completeContainsCounter += 1

print(completeContainsCounter)


