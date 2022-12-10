filecontent = open("input.txt", "r")

class Mover:
    def __init__(self):
        self.x = 0
        self.y = 0

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def move(self, direction, steps):
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
        print(self.x, self.y)

    def follow(self, x, y):
        deltaX = self.x - x
        deltaY = self.y - y

        if abs(deltaX) > 0 and abs(deltaY) > 0:
            print("diagonal move!")
        elif abs(deltaX) > 0:
            print("horisontal move")
        elif abs(deltaY) > 0:
            print("vertical move")


        print(deltaX, deltaY)


head = Mover()
tail = Mover()

print("Before for loop")
for line in filecontent:
    input = line.replace("\n", "").split(" ")
    print(input[0])
    print(input[1])
    head.move(input[0], input[1])
    tail.follow(head.x, head.y)


