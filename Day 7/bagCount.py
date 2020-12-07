from collections import Counter

bagInput = [line.strip('\n') for line in open("input.txt", "r")]
validBags = set()
checked = set()
cleanInput = []
temp = ""

bagInput = [x.replace(' bags contain', ',') for x in bagInput]
bagInput = [x.replace(' bag.', ' ') for x in bagInput]
bagInput = [x.replace(' bags.', '') for x in bagInput]
bagInput = [x.replace(' bags', '') for x in bagInput]
bagInput = [x.replace(' bag', '') for x in bagInput]
bagInput = [x.split(', ') for x in bagInput]

for bag in bagInput:
    bag[:] = [x.strip() for x in bag]

for i in bagInput:
    line = []
    for j in i:
        if j[0].isdigit():
            line.append(j[2:])
        else:
            line.append(j)
    cleanInput.append(line)

def findParentBags(childBag):
    for bags in cleanInput:
        for bag in bags:
            if childBag == bag and bags[0] != childBag:
                validBags.add(bags[0])
                findParentBags(bags[0])

findParentBags('shiny gold')

print(len(validBags))