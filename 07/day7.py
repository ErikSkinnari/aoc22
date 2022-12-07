filecontent = open("input.txt", "r")

commands = []

for line in filecontent:
    commands.append(line.replace("\n", ""))

print(commands)

directories = []
currentDirectory = {}

def isCommand(line):
    return line.split(" ")[0] == "$"

def isDirectory(line):
    return line.split(" ")[0] == "dir"

def changeDirectory(path):
    for directory in directories:
        if directory.path == path:
            currentDirectory = directory
            break
    if currentDirectory.path != path:
        print("Could not change dir to: ", path)

def parseCommand(line):
    arguments = line.split(" ")
    command = arguments[1]
    param = ""
    if command == "cd":
        param = arguments[2]
        if path == "..":
            currentDirectory = changeDirectory(currentDirectory.parent)
        else:
            currentDirectory = changeDirectory(currentDirectory.path + "/" + path)
    elif command == "ls":
        # create all files and folders
        print("todo")

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def getSize():
        return self.size

class Directory:
    def __init__(self, parentPath, path):
        self.parentPath = parentPath        
        self.path = path
        self.files = []
        self.directories = []

    def getSize():
        totalSize = 0

        for directory in self.directories:
            totalSize += directory.getSize()
        for f in self.files:
            totalSize += f.getSize()

        return totalSize


def getFolder(folderName):
    print("todo")



