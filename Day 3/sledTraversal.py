sledInput = [line.strip('\n') for line in open("sledInput.txt", "r")]

endpoints = []
curX = 0

for row in sledInput:
    endpoints.append(row[curX%31])
    curX += 3

print(endpoints.count('#'))