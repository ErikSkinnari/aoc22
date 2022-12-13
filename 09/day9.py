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

    def moveHead(self, direction, steps):
        print("Move")
        print("Direction: ", direction)
        print("Steps: ", steps)

        for i in range(int(steps)):
            match direction:
                case "U":
                    self.up()
                case "D":
                    self.down()
                case "L":
                    self.left()
                case "R":
                    self.right()
                    
            print("After movement:")
            print("Head: ", self.x, self.y)
            self.moveTail()

    def moveTail(self):
        deltaX = self.x - self.tailX
        deltaY = self.y - self.tailY

        print("Delta: ", deltaX, deltaY)
        changeX = 0
        if deltaX < 0:
            changeX = -1
        elif deltaX > 0:
            changeX = 1

        changeY = 0
        if deltaY < 0:
            changeY = -1
        elif deltaY > 0:
            changeY = 1
            
        if abs(deltaX) > 1 and abs(deltaY) == 0:
            print("horisontal move")
            self.tailX += changeX
        elif abs(deltaY) > 1 and abs(deltaX) == 0:
            print("vertical move")
            self.tailY += changeY
        elif (abs(deltaX) > 0 and abs(deltaY) > 1) or (abs(deltaX) > 1 and abs(deltaY) > 0):
            print("diagonal move!")
            self.tailX += changeX
            self.tailY += changeY
        print("tail: ", self.tailX, self.tailY)

        for i in range(5):
            for j in range(6):
                if self.y == i and self.x == j:
                    print("H", end="")
                elif self.tailY == i and self.tailX == j:
                    print("T", end="")
                else:
                    print(".", end="")
            print()

        self.visited.append(Vector(self.tailX, self.tailY))


head = Mover()

print("Before for loop")
for line in filecontent:
    input = line.replace("\n", "").split(" ")
    print(input[0])
    print(input[1])
    head.moveHead(input[0], input[1])


#for spot in head.visited:
#    print(spot)
#    if spot not in visitedSpots:
#        visitedSpots.append(spot)
unique = list(set(head.visited))

print(len(unique))

