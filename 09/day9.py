#filecontent = open("testinput.txt", "r")
filecontent = open("input.txt", "r")
class Vector:
    def __init__(self, x, y ):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + " | y: " + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(('x', self.x, 'y', self.y))

def getChangeValue(deltaValue):
    if deltaValue < 0:
        return -1
    elif deltaValue > 0:
        return 1
    return 0

def calculateChange(deltaX, deltaY, changeX, changeY):
    change = [ 0, 0 ]
    if abs(deltaX) > 1 and abs(deltaY) == 0:
        change = [changeX, 0]
    elif abs(deltaY) > 1 and abs(deltaX) == 0:
        change = [ 0, changeY]
    elif (abs(deltaX) > 0 and abs(deltaY) > 1) or (abs(deltaX) > 1 and abs(deltaY) > 0):
        change = [ changeX, changeY ]
    return change

class Mover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tailX = 0
        self.tailY = 0
        self.visited = []

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def move(self, x, y):
        if x == 0 and y == 0:
            return [0, 0]
        self.x += x
        self.y += y

        return [self.x, self.y] # added part 2

class Follower():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = []

    def follow(self, xToFollow, yToFollow):
        deltaX = xToFollow - self.x
        deltaY = yToFollow - self.y
        changeX = getChangeValue(deltaX)
        changeY = getChangeValue(deltaY)
        movement = calculateChange(deltaX, deltaY, changeX, changeY)

        self.x += movement[0]
        self.y += movement[1]
        self.visited.append(Vector(self.x, self.y))
        return [ self.x, self.y ]


def translateInput():
    instructions = []

    for line in filecontent:
        input = line.replace("\n", "").split(" ")
        for i in range(int(input[1])):
            match input[0]:
                case "U":
                    instructions.append([0, 1])
                case "D":
                    instructions.append([0, -1])
                case "L":
                    instructions.append([-1, 0])
                case "R":
                    instructions.append([1, 0])

    return instructions

head = Mover()
one = Follower()
two = Follower()
three = Follower()
four = Follower()
five = Follower()
six = Follower()
seven = Follower()
eight = Follower()
nine = Follower()

interpretedInstructions = translateInput()


for line in interpretedInstructions:
    print()
    print("INSTRUCTION")
    print(line)
    print("HEAD")
    headTailPos = head.move(line[0], line[1])
    print(headTailPos)
    print("ONE")
    oneTailPos = one.follow(headTailPos[0], headTailPos[1])
    print(one.x, one.y)
    print(oneTailPos)
    twoTailPos = two.follow(oneTailPos[0], oneTailPos[1])
    threeTailPos = three.follow(twoTailPos[0], twoTailPos[1])
    fourTailPos = four.follow(threeTailPos[0], threeTailPos[1])
    fiveTailPos = five.follow(fourTailPos[0], fourTailPos[1])
    sixTailPos = six.follow(fiveTailPos[0], fiveTailPos[1])
    sevenTailPos = seven.follow(sixTailPos[0], sixTailPos[1])
    eightTailPos = eight.follow(sevenTailPos[0], sevenTailPos[1])
    ninePos = nine.follow(eightTailPos[0], eightTailPos[1])
    print("NINE")
    print(ninePos)


unique = list(set(nine.visited))
#unique = list(set(one.visited))
print(len(unique))

