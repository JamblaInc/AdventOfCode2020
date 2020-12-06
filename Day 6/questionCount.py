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
    newInput.append(len(set("".join(i.split()))))


print(sum(newInput))