"""
My Aunt Sue has:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

sue = dict()
sue.setdefault('children',    3)
sue.setdefault('cats',        7)
sue.setdefault('samoyeds',    2)
sue.setdefault('pomeranians', 3)
sue.setdefault('akitas',      0)
sue.setdefault('vizslas',     0)
sue.setdefault('goldfish',    5)
sue.setdefault('trees',       3)
sue.setdefault('cars',        2)
sue.setdefault('perfumes',    1)

for i in open("day16.txt").read().split("\n"):
    things = i[i.index(":")+2:].split(", ")
    mysue = True
    for j in things:
        j = j.split(": ")
        # part 2
        if j[0] == "cats" or j[0] == "trees":
            if sue[j[0]] >= int(j[1]):
                mysue = False
                break
        elif j[0] == "pomeranians" or j[0] == "goldfish":
            if sue[j[0]] <= int(j[1]):
                mysue = False
                break
        # for part 1 just remove above and "el" from the statement below
        elif sue[j[0]] != int(j[1]):
            mysue = False
            break
    if mysue:
        print(i)
        break
