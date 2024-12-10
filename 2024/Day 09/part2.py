import os

FILE_NAMES = ['small', 'large']
YEAR = 2024
DAY = "Day 09"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)
    
    def createDiskMap():
        diskMap = []
        flag = True
        bid = 0
        for key in ar[0]:
            if flag:
                diskMap.append([bid, int(key)])
                bid += 1
            else:
                diskMap.append(['.', int(key)])
            flag = not flag
        return diskMap
    
    diskMap = createDiskMap()
    
    def insertFileIfPossible(fileIdx):
        nonlocal diskMap
        fileToMove = diskMap[fileIdx][:]
        indexToInsert = -1
        idx = 0
        while idx < fileIdx:
            if diskMap[idx][0] == '.' and diskMap[idx][1] >= fileToMove[1]:
                indexToInsert = idx
                break
            idx += 1
        
        if indexToInsert != -1:
            diskMap[fileIdx][0] = '.'
            diskMap[indexToInsert][1] -= fileToMove[1]
            if diskMap[indexToInsert][1] == 0:
                diskMap.pop(indexToInsert)
            diskMap.insert(indexToInsert, fileToMove)
    
    def getIndexOfFileId(fileId):
        for idx, _file in enumerate(diskMap):
            if _file[0] == fileId:
                return idx
        return None
    
    fileId = diskMap[-1][0]
    while fileId:
        idx = getIndexOfFileId(fileId)
        insertFileIfPossible(idx)
        fileId -= 1
    
    def convertMapToStr():
        disk = []
        for num, times in diskMap:
            if num == '.':
                num = 0
            disk.extend([num] * times)
        return disk

    disk = convertMapToStr()
    
    def checksum(disk):
        ans = 0
        for idx, num in enumerate(disk):
            ans += idx * num
        return ans
        
    return checksum(disk)        
        
for name in FILE_NAMES:
    print(name, solve(name))
