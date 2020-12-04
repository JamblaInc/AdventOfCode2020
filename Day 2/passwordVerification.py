passwordInput = [line.strip('\n') for line in open("passwordInput.txt", "r")]
passwordInput = [line.split(' ') for line in passwordInput]
passwordList = []
count = 0

for line in passwordInput:
    inputDict = {}
    inputDict['min'], inputDict['max'] = line[0].split('-')
    inputDict['letter'] = line[1][0]
    inputDict['password'] = line[2]
    passwordList.append(inputDict)

for i in passwordList:
    if int(i['min']) <= int(i['password'].count(i['letter'])) <= int(i['max']):
        count +=1

print(count)