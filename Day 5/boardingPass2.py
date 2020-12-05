boardingPassInput = [line.strip('\n') for line in open('boardingPassInput.txt', 'r')]
allIds = []

def getRow(inputString):
    nums = list(range(128))
    for i in inputString[:7]: 
        if (i == "F"):
            # Lower half
            nums = nums[:len(nums)/2]
        else:
            # Upper half
            nums = nums[len(nums)/2:]
    return nums[0]

def getSeat(inputString):
    nums = list(range(8))
    for i in inputString[7:]: 
        if (i == "L"):
            # Lower half
            nums = nums[:len(nums)/2]
        else:
            # Upper half
            nums = nums[len(nums)/2:]
    return nums[0]

for i in boardingPassInput:
    row = getRow(i)
    seat = getSeat(i)
    allIds.append(row*8+seat)

allIds.sort()
print([x for x in range(allIds[0], allIds[-1]+1) if x not in allIds])