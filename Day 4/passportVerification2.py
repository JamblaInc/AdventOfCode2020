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

validPassports = 0

for i in dicts:
    if not (i.get('ecl') is None or i.get('ecl') not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or i.get('pid') is None or len(i.get('pid')) != 9 or i.get('pid').isdigit() == False or i.get('eyr') is None or int(i.get('eyr')) < 2020 or int(i.get('eyr')) > 2030 or i.get('hcl') is None or i.get('hcl')[0] != '#' or i.get('hcl')[1:].isalnum() == False or len(i.get('hcl')[1:]) != 6 or i.get('byr') is None or int(i.get('byr')) < 1920 or int(i.get('byr')) > 2002 or i.get('iyr') is None or int(i.get('iyr')) > 2020 or int(i.get('iyr')) < 2010) :
        if i.get('hgt') is not None:  
            if "cm" in i.get('hgt')[-2:] and 150 <= int(i.get('hgt')[:-2]) <= 193 :
                validPassports += 1
            if "in" in i.get('hgt')[-2:] and 59 <= int(i.get('hgt')[:-2]) <= 76 :
                validPassports += 1
        
print(validPassports)