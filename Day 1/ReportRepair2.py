reportInput = [int(line.strip('\n')) for line in open("reportInput.txt", "r")]

for i in reportInput:
    for j in reportInput:
        for k in reportInput:
            if i + j + k == 2020:
                print(i,j,k)
                print(i*j*k)
