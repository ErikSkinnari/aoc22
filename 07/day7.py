import json

filecontent = open("input.txt", "r")

commands = []

for line in filecontent:
    commands.append(line.replace("\n", ""))
    print(line)

print(commands)
directories = []

currentDirectory = {}


def isCommand(line):
    return line.split(" ")[0] == "$"


def isDirectory(line):
    return line.split(" ")[0] == "dir"


def changeDirectory(path):
    #print("changing dir to: ", path)
    if len(directories) == 0 and path == "/":
        rootDir = Directory("", "/")
        directories.append(rootDir)
        return rootDir
    
    for directory in directories:
        if directory.path == path:
            #print("found dir to switch to", directory)
            currentDirectory = directory
            #print("now currentdirectory is set to: ", currentDirectory)
            return currentDirectory


def parseCommands():
    print("Parsing starts")

    while len(commands) > 0:
        #print("Total # of dirs: ", len(directories))
        instruction = commands.pop(0).replace("\n", "") # remove line from list of commands
        #print("Instruction: ", instruction)
        arguments = instruction.split(" ")
        #print(arguments)
        command = arguments[1]
        param = ""
        if command == "cd":
            param = arguments[2]
            #print("cd command, param: ", param)
            if param == "/":
                currentDirectory = changeDirectory(param)
            elif param == "..":
                #print("cd .. current dir", currentDirectory)
                parentPath = currentDirectory.parentPath
                #print("ParentPath: ", parentPath)
                currentDirectory = changeDirectory(parentPath)
                #print("CurrentDirectory after cd .. : ", currentDirectory)
            else:
                newDir = (currentDirectory.path + "/" + param).replace("//", "/")
                #print(newDir)
                currentDirectory = changeDirectory(newDir)
                #print(currentDirectory)
        
        elif command == "ls":
            while True:
                #if len(commands) < 3:
                 #   print(commands)
                  #  break
                row = commands.pop(0).replace("\n", "")
                #print("Row: ", row)
                #print("CurrentDir: ", currentDirectory)
                
                if isCommand(row):
                    #print("Row is command, putting back in to commands: ", row)
                    commands.insert(0, row)
                    break

                fileInfo = row.split(" ")
                if isDirectory(row):
                    dirPath = ""
                    if currentDirectory.path == "/":
                        dirPath = currentDirectory.path + fileInfo[1]
                    else:
                        dirPath = currentDirectory.path + "/" + fileInfo[1]
                    #print("CurrentDirectory path: ", currentDirectory.path)
                    #print("dirPath: ", dirPath)
                    newDirectory = Directory(currentDirectory.path, dirPath)
                    directories.append(newDirectory)
                    currentDirectory.directories.append(newDirectory)
                    #print("New directory created: ", dirPath)
                    #print("Total number of directories: ", len(directories))
                else:
                    filePath = currentDirectory.path + "/" + fileInfo[1]
                    newFile = File(filePath, int(fileInfo[0]))
                    currentDirectory.files.append(newFile)
                    #print("New file created: ", filePath)
                    #print("Total number of files in current directory: ", len(currentDirectory.files))
                if len(commands) == 0:
                    break

    ### A Real mess down here, I know. Just want to get this done! :/
    currentDirectory = changeDirectory("/")
    print(currentDirectory.path)
    print(currentDirectory.getSize())

    print("summing up")
    sumTotalUnder100000 = 0

    for d in directories:
        size = d.getSize()
        if size <= 100000:
            sumTotalUnder100000 += size
            #print(size)
    #print(sum)

    spaceNeeded = 30000000
    candidatesForDeletion = []
    sizes = []
    print(spaceNeeded)
    for d in directories:
        size = int(d.getSize())
        print(size)
        #if size >= spaceNeeded:
        sizes.append(size)
    totalUsed = currentDirectory.getSize()
    print("totalUsed: ", totalUsed)

    total = 70000000

    free = total - totalUsed
    print("free: ", free)

    toDelete = spaceNeeded - free

    print("To delete: ", toDelete)

    for s in sizes:
        if s >= toDelete:
            candidatesForDeletion.append(s)

    print(sorted(candidatesForDeletion)[0])




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

