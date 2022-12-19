class Directory:
    def __init__(self,name,parent):
        self._parent = parent
        self.children = []
        self.childNames = []
        self.own_size = 0
        self.name = name
        if parent is not None:
            parent.addChild(self)

    def addFile(self,fileSize):
        self.own_size += fileSize

    def getTotalSize(self):
        size = self.own_size
        for subdir in self.children:
            size += subdir.getTotalSize()
        return size

    def addChild(self,obj):
        if obj.name not in self.childNames:
            self.children.append(obj)
            self.childNames.append(obj.name)
            obj.parent = self
        

rootDir = Directory('/',None)
currentDir = rootDir
dirList = []
with open('input.txt','r') as f:
    for line in f:
        tokens = line.split()
        if tokens[0] == '$':
            #Its a command
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    currentDir = currentDir.parent
                elif tokens[2] == '/':
                    currentDir = rootDir
                else:
                    idx = currentDir.childNames.index(tokens[2])
                    currentDir = currentDir.children[idx]
        else: 
            # we must be in a directory listing.
            if tokens[0] == 'dir':
                if tokens[1] not in currentDir.childNames:
                    newDir = Directory(tokens[1],currentDir)
                    dirList.append(newDir)
                    currentDir.addChild(newDir)
            else:
                currentDir.addFile(int(tokens[0]))


##PART 2
totalSize = rootDir.getTotalSize()
freeSpace = 70000000-totalSize
neededSpace = 30000000-freeSpace


minDeletion = 70000000
for dir in dirList:
    totalDirSize = dir.getTotalSize()
    if totalDirSize > neededSpace and totalDirSize < minDeletion:
        minDeletion = totalDirSize

print(minDeletion)
