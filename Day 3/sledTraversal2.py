sledInput = [line.strip('\n') for line in open("sledInput.txt", "r")]

endpoints = []
product = 1

def getNextI(i, d):
    return i+d

def getNextJ(j, r):
    return j+r

def getTrees(rightSteps, downSteps):
    i, j = 0, 0
    endpoints = []
    while getNextI(i, downSteps) < len(sledInput):
        i = getNextI(i, downSteps)
        j = getNextJ(j, rightSteps) 
        endpoints.append(sledInput[i][j%31])
    return endpoints.count('#')

product = getTrees(1,1)*getTrees(3, 1)*getTrees(5, 1)*getTrees(7, 1)*getTrees(1, 2)

print(getTrees(1, 1))
print(getTrees(3, 1))
print(getTrees(5, 1))
print(getTrees(7, 1))
print(getTrees(1, 2))
print(product)