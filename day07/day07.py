def Int(s):
    try:
        a = int(s)
        return a
    except ValueError:
        return -1


f = open("day07.txt")
f = f.readlines()

reg = []

for i in range(len(f)):
    line_array = f[i].split()
    reg.append([line_array[-1], -1, line_array[:-2]])
# reg.sort(key=lambda x: (len(x[2]), x[0]))

while True:
    for i in reg:
        command = i[2]
        if len(command) == 3:
            a = [r[0] for r in reg]
            t1 = Int(command[0])
            t2 = Int(command[-1])
            if t1 < 0:
                x1 = reg[a.index(command[0])]
                t1 = x1[1]
            if t2 < 0:
                x2 = reg[a.index(command[-1])]
                t2 = x2[1]
            if t1 != -1 and t2 != -1:
                if i[1] == -1:
                    print(i)
                if command[1] == 'AND':
                    i[1] = t1 & t2
                elif command[1] == 'OR':
                    i[1] = t1 | t2
                elif command[1] == 'LSHIFT':
                    i[1] = t1 << t2
                    if i[1] > 2 ** 16: i[1] %= 2 ** 16 + 1
                elif command[1] == 'RSHIFT':
                    i[1] = t1 >> t2

        else:
            a = [r[0] for r in reg]
            value = Int(command[-1])
            if value < 0:
                register_to_get_value_from = reg[a.index(command[-1])]
                value = register_to_get_value_from[1]
            if value >= 0:
                if i[1] == -1:
                    print(i)
                i[1] = value if len(command) == 1 else ~value % 2 ** 16

    v = [r[1] for r in reg]
    if -1 not in v:
        a = [r[0] for r in reg]
        print(reg[a.index('a')][1])
        break
