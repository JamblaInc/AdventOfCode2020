bagInput = [line.strip('\n') for line in open("input.txt", "r")]
validBags = []
newInput = []
temp = ""

bagInput = [x.replace(' bags contain', ',') for x in bagInput]
bagInput = [x.replace('.', ' ') for x in bagInput]
bagInput = [x.split(', ') for x in bagInput]

for i in bagInput:
    print(i)
