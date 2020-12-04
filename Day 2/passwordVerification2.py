passwordInput = [line.strip('\n') for line in open("passwordInput.txt", "r")]
passwordInput = [line.split(' ') for line in passwordInput]
passwordList = []
count = 0

for line in passwordInput:
    inputDict = {}
    inputDict['char1'], inputDict['char2'] = line[0].split('-')
    inputDict['letter'] = line[1][0]
    inputDict['password'] = line[2]
    passwordList.append(inputDict)

for i in passwordList:
    if bool(str(i['letter']) == str(i['password'][int(i['char1']) - 1])) ^ bool(str(i['letter']) == str(i['password'][int(i['char2']) - 1])):
        count +=1

print(count)