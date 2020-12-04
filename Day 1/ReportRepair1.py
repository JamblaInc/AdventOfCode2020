reportInput = [int(line.strip('\n')) for line in open("reportInput.txt", "r")]

for i in reportInput:
    for j in reportInput:
        if i + j == 2020:
            print(i,j)
            print(i*j)
