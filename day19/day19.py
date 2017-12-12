reactions = list()
newmolecules = set()

molecule = ""
for i in open("day19.txt").read().split("\n"):
    if "=>" in i:
        a, _, b = i.split(" ")
        reactions.append((a, b))
    else:
        molecule = i

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

# part 2

idx = 0
atoms = list()
countatoms = 0
for _ in range(len(molecule)):
    countatoms += 1
    tmp = molecule[idx]
    idx += 1
    while idx < len(molecule) and molecule[idx].islower():
        tmp += molecule[idx]
        idx += 1
    if tmp not in atoms:
        atoms.append(tmp)
    if idx >= len(molecule):
        break

rn = molecule.count('Rn')
ar = molecule.count('Ar')
y = molecule.count('Y')

# thanks to the /u/askalski
print("part 2:", countatoms - (rn + ar + 2*y) - 1)
