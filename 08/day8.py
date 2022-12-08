filecontent = open("input.txt", "r")

forrest = []

for line in filecontent:
    forrest.append(line.replace("\n", ""))

def isHiddenBehindAnotherTree(height, otherTrees):
    for tree in otherTrees:
        if int(tree) >= int(height):
            return True
    return False

def getVerticalTrees(x):
    trees = []
    for treeline in forrest:
        trees.append(treeline[x])
    return trees

def isVisibleEast(x, y):
    easternTrees = forrest[y]
    if x == len(easternTrees) - 1:
        return True
    return isHiddenBehindAnotherTree(easternTrees[x], easternTrees[x + 1:]) == False

def isVisibleWest(x, y):
    if x == 0:
        return True
    westernTrees = forrest[y]
    return isHiddenBehindAnotherTree(westernTrees[x], westernTrees[0: x]) == False

def isVisibleNorth(x, y):
    if y == 0:
        return True
    northernTrees = getVerticalTrees(x)[0 : y]
    return isHiddenBehindAnotherTree(forrest[y][x], northernTrees) == False

def isVisibleSouth(x, y):
    if y == len(forrest) - 1:
        return True
    southernTrees = getVerticalTrees(x)[y + 1:]
    return isHiddenBehindAnotherTree(forrest[y][x], southernTrees) == False


print("forrest is this high: ", len(forrest))

# Top
# 332003300013411421030123310000325304355245416315402454123304251100551413414301042114403240340202013
# 130120131034131214123330450045513234151453520504226501101432120555550112535000130014212133321332113

# Bottom
# 132200122232433121333410132153131541542513264261463154353021340403623114231305043110312440012243111
# 001320030221212412130340411450015410126162032430413232552634423102222044153052245310344121344231122

print("Should be visible:")
print(isVisibleEast(-8, 0))
print(isVisibleWest(12, 0))
print(isVisibleNorth(3, 1))
print(isVisibleSouth(0, len(forrest) - 2))

print("Should not be visible:")
print(isVisibleEast(-3, 1))
print(isVisibleWest(4, 1))
print(isVisibleNorth(6, 1))
print(isVisibleSouth(4, len(forrest) - 2))

def isVisible(x, y):
    return isVisibleEast(x, y) or isVisibleWest(x, y) or isVisibleNorth(x, y) or isVisibleSouth(x, y)

height = len(forrest)
width = len(forrest[0])

visibleTrees = 0

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            visibleTrees += 1
        elif j == 0 or j == width - 1:
            visibleTrees += 1
        else:
            if isVisible(j, i):
                visibleTrees += 1

print("Visible trees: ", visibleTrees)
