
class Instruction():
    def __init__(self, opType, registerChange = 0):
        self.opType = opType
        self.processTime = 0
        if opType == "noop":
            self.processTime = 1
        elif opType == "addx":
            self.processTime = 2

        self.progress = 0
        self.registerChange = registerChange

    def updateProgress(self):
        self.progress += 1
        return self.isDone()

    def isDone(self):
        return self.progress >= self.processTime

    def __str__(self):
        return "Instruction: " + self.opType + " | registerChange: " + str(self.registerChange)

fileinput = open("input.txt", "r")
instructions = []

for line in fileinput:
    instructionDetails = line.replace("\n", "").split(" ")
    if len(instructionDetails) < 2:
        instruction = Instruction(instructionDetails[0])
    else:
        instruction = Instruction(instructionDetails[0], instructionDetails[1])

    instructions.append(instruction)

currentInstruction = {}
xBuffer = 1
cpucycle = 0
currentInstruction = instructions.pop(0)
signalStrengths = []
pixels = ''

while True:
    cpucycle += 1

    pixelposition = (cpucycle - 1) % 40
    if pixelposition in [ xBuffer - 1, xBuffer, xBuffer + 1]:
        pixels += "#"
    else:
        pixels += "."

    if cpucycle == 20 or (cpucycle - 20) % 40 == 0:                
        signalStrength = cpucycle * xBuffer
        signalStrengths.append(signalStrength)
        print("cpucycle: " + str(cpucycle) + " | X-value: " + str(xBuffer) + " | Calculated Value: " + str(signalStrength))

    if currentInstruction.opType == "noop":
        if len(instructions):
            currentInstruction = instructions.pop(0)
        else:
            break
    else:
        instructionFinished = currentInstruction.updateProgress()
        if instructionFinished:
            xBuffer += int(currentInstruction.registerChange)
            if len(instructions):
                currentInstruction = instructions.pop(0)
            else:
                break
#    print(str(cpucycle) + " | x: " + str(xBuffer)) # Debugging

signalSum = 0
for s in signalStrengths:
    signalSum += s
print("Signal streangth sum (part1): ", signalSum)
print("Part 2:")
for i in range(6):
    line = ""
    for j in range(40):
        line += pixels[0].replace("\n", "")
        newPixels = pixels[1:]
        pixels = newPixels
    print(line)
