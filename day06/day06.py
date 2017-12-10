def get(a):
    x, y = str(a).split(',')
    x = int(x)
    y = int(y)
    return x, y


f = open("day06.txt")
f = f.readlines()

square = 1000

lights = [[0 for j in range(square)]for i in range(square)]

print(f[0])

for w in range(len(f)):
    instr = f[w].split(' ')
    if len(instr) == 5:
        begin = get(instr[2])
        end = get(instr[4])
        for i in range(begin[0], end[0]+1):
            for j in range(begin[1], end[1]+1):
                if instr[1] == 'on':
                    lights[i][j] += 1
                else:
                    if lights[i][j] != 0:
                        lights[i][j] -= 1
    else:
        begin = get(instr[1])
        end = get(instr[3])
        for i in range(begin[0], end[0]+1):
            for j in range(begin[1], end[1]+1):
                lights[i][j] += 2

sum = 0
for i in range(square):
    for j in range(square):
        sum += lights[i][j]

print('end', sum)
