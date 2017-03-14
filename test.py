with open('Text.txt') as f:
    arr = []
    for line in f:
        sec = [int(i) for i in line.split()]
        for ins in sec:
            arr.append(ins)


print(arr)
