filecontent = open("input.txt", "r")

xValues = []
yValues = []

rockPaths = []
for line in filecontent:
    print(line)
    rockStructurePathNodes = line.replace("\n", "").split(" -> ")

    for node in rockStructurePathNodes:
        print(node)
        x, y = node.split(",")
        print(x)
        print(y)
        xValues.append(int(x))
        yValues.append(int(y))

    for i in range(1, len(rockStructurePathNodes) - 1):
        rockPaths.append([rockStructurePathNodes[i-1], rockStructurePathNodes[i]])

        
print("X:")
print("xValues.len: ", len(xValues))
print(min(xValues))
print(max(xValues))

print("Y:")
print("yValues.len: ", len(yValues))
print(min(yValues))
print(max(yValues))

for path in rockPaths:
    print(path)
#print(len(rockPaths))

caveMatrix = []

for i in range(0, max(yValues)):
    caveLevel = []
    for j in range(min(xValues), max(xValues)):
        caveLevel.append(".")
    caveMatrix.append(caveLevel)

xOffset = min(xValues)

print("cave height: ", len(caveMatrix))
print("cave width: ", len(caveMatrix[0]))
# Place down rocks
for path in rockPaths:
    startPos = path[0]
    stopPos = path[1]

    start = startPos.split(",")
    x1 = int(start[0])
    y1 = int(start[1])
   
    stop = stopPos.split(",")
    x2 = int(stop[0])
    y2 = int(stop[1])

    if x1 == x2:
        for yPos in range(y1 - 1, y2 - 1):
            caveMatrix[yPos][x1 - xOffset] = "#"
    else:
        for xPos in range(x1 - xOffset, x2 - xOffset):
            print(xPos)
            print(y1)
            caveMatrix[y1 - 1][xPos] = "#"

    


for line in caveMatrix:
    for spot in line:
        print(spot, end="")
    print()



#for path in rockPaths:


class Sand:
    def __init__(self):
        self.isResting = false
        self.x = 500
        self.y = 0

    #def fall(self):

