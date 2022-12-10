filecontent = open("input.txt", "r")

forrest = []

for line in filecontent:
    forrest.append(line.replace("\n", ""))
forrestHeight = len(forrest)
forrestWidth = len(forrest[0])

class Tree:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = int(height)

    def getScenicScore(self):
        if (self.x == 0 or self.y == 0 or self.x == forrestWidth - 1 or self.y == forrestHeight - 1):
            return 0
        west = calculateScore(self.height, getWesternTrees(self.x, self.y))
        north = calculateScore(self.height, getNorthernTrees(self.x, self.y))
        east = calculateScore(self.height, getEasternTrees(self.x, self.y))
        south = calculateScore(self.height, getSouthernTrees(self.x, self.y))

        calculatedScore = west * north * east * south
        return calculatedScore


def reverseString(string):
    return string[::-1]

def calculateScore(height, treeLine):
    score = 0
    for i in range(len(treeLine)):
        score += 1
        if int(treeLine[i]) >= int(height):
            break
    return int(score)

### Get list of trees in a direction ###
def getWesternTrees(x, y):
    westernTrees = forrest[y][0:x]
    return reverseString(westernTrees)

def getNorthernTrees(x, y):
    verticalTrees = getVerticalTrees(x)
    return reverseString(verticalTrees[0: y])

def getEasternTrees(x, y):
    return forrest[y][x + 1:]

def getSouthernTrees(x, y):
    return getVerticalTrees(x)[y + 1:]


### Get trees in a vertical line by x value ###
def getVerticalTrees(x):
    trees = ""
    for treeline in forrest:
        trees += treeline[x]
    return trees

def getTreeHeight(x, y):
    return forrest[y][x]


### Calculate visibility functions ####
def isVisibleEast(x, y):
    easternTrees = getEasternTrees(x, y)
    if x == forrestWidth - 1:
        return True
    height = getTreeHeight(x, y)
    return isHiddenBehindAnotherTree(height, easternTrees) == False

def isVisibleWest(x, y):
    if x == 0:
        return True
    westernTrees = getWesternTrees(x, y)
    height = getTreeHeight(x, y)
    return isHiddenBehindAnotherTree(height, westernTrees) == False

def isVisibleNorth(x, y):
    if y == 0:
        return True
    northernTrees = getNorthernTrees(x, y)
    height = getTreeHeight(x, y)
    return isHiddenBehindAnotherTree(height, northernTrees) == False

def isVisibleSouth(x, y):
    if y == forrestHeight - 1:
        return True
    southernTrees = getSouthernTrees(x, y)
    height = getTreeHeight(x, y)
    return isHiddenBehindAnotherTree(height, southernTrees) == False

def isHiddenBehindAnotherTree(height, otherTrees):
    isVisible = True
    for tree in otherTrees:
        if int(tree) >= int(height):
            isVisible = False
    return isVisible == False


print("Tests :)")
print("Should be visible:")
print("Is Visible: ", isVisibleEast(-8, 0))
print("Is Visible: ", isVisibleWest(12, 0))
print("Is Visible: ", isVisibleNorth(3, 1))
print("Is Visible: ", isVisibleSouth(0, len(forrest) - 2))

print("Should not be visible:")
print("Is Visible: ", isVisibleEast(-3, 1))
print("Is Visible: ", isVisibleWest(4, 1))
print("Is Visible: ", isVisibleNorth(6, 1))
print("Is Visible: ", isVisibleSouth(4, len(forrest) - 2))

def isVisible(x, y):
    return isVisibleEast(x, y) or isVisibleWest(x, y) or isVisibleNorth(x, y) or isVisibleSouth(x, y)

visibleTrees = 0
trees = []
treescores = []

for i in range(forrestHeight):
    for j in range(forrestWidth):

        t = Tree(j, i, getTreeHeight(j, i))
        trees.append(t)

        visible = False
        if i == 0 or i == forrestHeight - 1 or j == 0 or j == forrestWidth - 1:
            visible = True
        else:
            if isVisible(j, i):
                visible = True
        if visible:
            visibleTrees += 1

highestScenicScore = 0
bestScoringTree = {}

for tree in trees:
    treeScore = tree.getScenicScore()
    if treeScore > highestScenicScore:
        highestScenicScore = treeScore
        bestScoringTree = tree

print("Best scenic score: ", highestScenicScore)
print("Visible trees: ", visibleTrees)


