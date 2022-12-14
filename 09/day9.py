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

def normalizeChange(value):
    if value < 0:
        return -1
    elif value > 0:
        return 1
    return 0

def calculateChange(deltaX, deltaY, changeX, changeY):
    if abs(deltaX) > 1 and abs(deltaY) == 0:
        return [changeX, 0]
    elif abs(deltaY) > 1 and abs(deltaX) == 0:
        return [ 0, changeY]
    elif (abs(deltaX) > 0 and abs(deltaY) > 1) or (abs(deltaX) > 1 and abs(deltaY) > 0):
        return [ changeX, changeY ]
    return [ 0, 0 ]

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

    #def moveHead(self, direction, steps): # step 1
    def move(self, x, y):
        if x == 0 and y == 0:
            return [0, 0]
        self.x += x
        self.y += y

        #        for i in range(int(steps)):
        #    match direction:
        #        case "U":
        #            self.up()
        #        case "D":
        #            self.down()
        #        case "L":
        #            self.left()
        #        case "R":
        #            self.right()
                    
            #print("After movement:")
            #print("Head: ", self.x, self.y)
        self.moveTail()
        return [self.tailX, self.tailY] # added part 2

    def moveTail(self):
        deltaX = self.x - self.tailX
        deltaY = self.y - self.tailY
        changeX = normalizeChange(deltaX)
        changeY = normalizeChange(deltaY)
        
        movement = calculateChange(deltaX, deltaY, changeX, changeY)
        print("movement")
        print(movement)
        self.tailX += movement[0]
        self.tailY += movement[1]
        self.visited.append(Vector(self.tailX, self.tailY))

class Follower():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = []

    def follow(self, followingX, followingY):
        deltaX = self.x - followingX
        deltaY = self.y - followingY
        changeX = normalizeChange(deltaX)
        changeY = normalizeChange(deltaY)
        movement = calculateChange(deltaX, deltaY, changeX, changeY)

        print("movement follower")
        print(movement)
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
    print(head.x, head.y)
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
print(len(unique))

