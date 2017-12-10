def chunker(str, size):
    return [str[pos:pos + size] for pos in range(0, len(str), size)]


reactions = list()
auxreactions = list()
newmolecules = set()

molecule = ""
for i in open("day19replaced.txt").read().split("\n"):
    if "=>" in i:
        a, _, b = i.split(" ")
        reactions.append((a, b))
    else:
        molecule = i

left = 'a'
for r in reactions:
    if len(r[1]) > 2:
        tmp = str(r[1])
        new = ''
        for chunk in chunker(tmp, 2):
            if len(chunk) == 1:
                new += chunk
                break
            if chunk in [r[1] for r in reactions]:
                # print("react", [r[1] for r in reactions].index(chunk))
                idx = [r[1] for r in reactions].index(chunk)
                new += reactions[idx][0]

            elif chunk in [r[1] for r in auxreactions]:
                # print(chunk, "aux", idx, auxreactions[idx])
                idx = [r[1] for r in auxreactions].index(chunk)
                new += auxreactions[idx][0]

            else:
                auxreactions.append((left, chunk))
                new += left
                left = chr(ord(left) + 1)
        print(r[0], tmp, new)
        reactions.append((r[0], new))

for i in auxreactions:
    print(i)

reactions = list(filter(lambda x: len(x[1]) == 2, reactions))
for i in reactions:
    print(i)

for i in reactions:
    if i[0] in molecule:
        c = molecule.count(i[0])
        prev = -1
        while c > 0:
            prev = molecule.index(i[0], prev + 1)
            c -= 1
            tmp = molecule
            tmp = tmp[0:prev] + tmp[prev:].replace(i[0], i[1], 1)
            newmolecules.add(tmp)

print("part 1:", len(newmolecules))
