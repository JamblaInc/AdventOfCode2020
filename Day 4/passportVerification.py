import re

passportInput = [line.strip('\n') for line in open("passportInput.txt", "r")]
cleansedInput = []
temp = ""
for x in passportInput:
    if re.match(r'^\s*$', x):
        cleansedInput.append(temp)
        temp = ""
    else:
        temp += x
        temp += " "

dicts = []
for x in cleansedInput:
    tempDict = dict(s.split(':', 1) for s in x.split())
    dicts.append(tempDict)

print(dicts)

validPassports = 0

for i in dicts:
    validPassports += 1
    if i.get('ecl') is None or i.get('pid') is None or i.get('eyr') is None or i.get('hcl') is None or i.get('byr') is None or i.get('iyr') is None or i.get('hgt') is None:
        validPassports -= 1
        
print(validPassports)