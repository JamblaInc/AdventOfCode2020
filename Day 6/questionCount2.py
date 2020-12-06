import re

passportInput = [line.strip('\n') for line in open("input.txt", "r")]
cleansedInput = []
newInput = []
temp = ""

for x in passportInput:
    if re.match(r'^\s*$', x):
        cleansedInput.append(temp)
        temp = ""
    else:
        temp += x
        temp += " "

for i in cleansedInput:
    tempArr = []
    [tempArr.append(set(x)) for x in i.split()]
    newInput.append(tempArr)

sumInput = []
for i in newInput:
    intersection_set = set.intersection(*i)
    sumInput.append(len(intersection_set))

print(sum(sumInput))
