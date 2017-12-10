import itertools as it


def getProductionsOf(t):
    init = list()
    for p in productions:
        if t == p[1] and p[0] not in init:
            init.append(p[0])
    return init


productions = list()

molecule = "O1PBP4822256225622PB51F81F82256225622222251FYF85148251P77BFYPBF85125171F8538P7BP7125382P77BP4YF8P71F85122F812F82515148FY251482256P1F8PB251482256251748F856562251482251F87BP7125382P71F8PBPB22562PB56P1F8562562562P7B51FYF822P1F8PB22PB5171F82P1F85122256212F8Y251F8B22256F8PBF8251F81222F851F871P48F"

for i in open("day19newproductions.txt").read().split("\n"):
    a, _, b = i.split(" ")
    productions.append((a, b))

s = list(molecule)

tab = list()

l = len(s)
for row in range(l):
    # first-type productions of the terminals in a string. It's the first row in tab
    if row == 0:
        tab.append([q for q in molecule])
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
        print(add)
