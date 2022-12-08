filecontent = open("input.txt", "r")
commands = []

for line in filecontent:
    commands.append(line.replace("\n", ""))

directories = []

currentDirectory = {}


def isCommand(line):
    return line.split(" ")[0] == "$"


def isDirectory(line):
    return line.split(" ")[0] == "dir"


def changeDirectory(path):
    if len(directories) == 0 and path == "/":
        rootDir = Directory("", "/")
        directories.append(rootDir)
        return rootDir
    
    for directory in directories:
        if directory.path == path:
            print("Switching to ", directory)
            return directory


def parseCommands():
    print("Parsing starts")

    while len(commands) > 0:
        instruction = commands.pop(0).replace("\n", "") # remove line from list of commands
        arguments = instruction.split(" ")
        command = arguments[1]
        param = ""
        if command == "cd":
            param = arguments[2]
            if param == "/":
                currentDirectory = changeDirectory(param)
            elif param == "..":
                parentPath = currentDirectory.parentPath
                currentDirectory = changeDirectory(parentPath)
            else:
                newDir = (currentDirectory.path + "/" + param).replace("//", "/")
                currentDirectory = changeDirectory(newDir)
        
        elif command == "ls":
            while True:
                row = commands.pop(0).replace("\n", "")
                
                if isCommand(row):
                    commands.insert(0, row)
                    break

                fileInfo = row.split(" ")
                if isDirectory(row):
                    dirPath = ""
                    if currentDirectory.path == "/":
                        dirPath = currentDirectory.path + fileInfo[1]
                    else:
                        dirPath = currentDirectory.path + "/" + fileInfo[1]
                    newDirectory = Directory(currentDirectory.path, dirPath)
                    directories.append(newDirectory)
                    currentDirectory.directories.append(newDirectory)
                else:
                    filePath = currentDirectory.path + "/" + fileInfo[1]
                    newFile = File(filePath, int(fileInfo[0]))
                    currentDirectory.files.append(newFile)
                if len(commands) == 0:
                    break

    ### A Real mess down here, I know. Just want to get this done! :/
    currentDirectory = changeDirectory("/")
    print("Result:")
    sumTotalUnder100000 = 0
    sizes = []

    for d in directories:
        size = int(d.getSize())
        sizes.append(size)
        if size <= 100000:
            sumTotalUnder100000 += size

    print("Part 1: ", sumTotalUnder100000)

    spaceNeeded = 30000000
    total = 70000000
    
    totalUsed = currentDirectory.getSize()
    print("totalUsed: ", totalUsed)

    free = total - totalUsed
    print("free: ", free)

    toDelete = spaceNeeded - free
    print("To delete: ", toDelete)

    candidatesForDeletion = []

    for s in sizes:
        if s >= toDelete:
            candidatesForDeletion.append(s)

    print("Part 2: ", sorted(candidatesForDeletion)[0])


class File:
    def __init__(self, path, size):
        self.path = path
        self.size = size

    def __str__(self):
        return f'File. Path: {self.path} and size: {self.size}'
        
    def getSize(self):
        return self.size

class Directory:
    def __init__(self, parentPath, path):
        self.parentPath = parentPath        
        self.path = path
        self.files = []
        self.directories = []
    def __str__(self):
        return f'Directory. Path: {self.path} and parent path {self.parentPath}'
    def getSize(self):
        totalSize = 0

        for directory in self.directories:
            #print(directory.getSize())
            totalSize += directory.getSize()
        for f in self.files:
            #print(f.getSize)
            totalSize += f.getSize()

        return totalSize


def getFolder(folderName):
    print("todo")

parseCommands()

