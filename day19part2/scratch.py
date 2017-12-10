import itertools as it


def getProductionsOf(t):
    init = list()
    for p in productions:
        if t == p[1] and p[0] not in init:
            init.append(p[0])
    return init


productions = list()

for i in open("scratch.txt").read().split("\n"):
    a, _, b = i.split(" ")
    productions.append((a, b))

s = list("abba")

tab = list()

l = len(s)
for row in range(l):
    # first-type productions of the terminals in a string. It's the first row in tab
    if row == 0:
        cells = list()
        for char in s:
            cells.append(getProductionsOf(char))
        tab.append(cells)
    else:
        add = list()
        for cellnum in range(l - row):
            cells = list()
            for j in range(row):
                product = it.product(tab[j][cellnum], tab[row - j - 1][cellnum + 1 + j])
                for q in product:
                    s = q[0] + q[1]
                    g = getProductionsOf(s)
                    new = list()
                    for g1 in g:
                        if g1 not in cells:
                            new.append(g1)
                    cells.extend(new)
            add.append(cells)
        tab.append(add)

for i in tab:
    print(i)
print()
