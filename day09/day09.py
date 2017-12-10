import numpy as np
import itertools


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


file = open("day09.txt")
file = file.readlines()

names = []

for i, l in enumerate(file):
    line = l[:-1].split(" ")
    names.append(line[0]) if line[0] not in names else None
    names.append(line[-3]) if line[-3] not in names else None

distance = np.zeros((len(names), len(names)))

for i, l in enumerate(file):
    line = l[:-1].split(" ")
    name1, name2 = names.index(line[0]), names.index(line[-3])
    distance[name1][name2] = int(line[-1])
    distance[name2][name1] = int(line[-1])

a = list(itertools.permutations(names))
minimum = 100000000
maximum = 0
for i in a:
    dist = 0
    for j in list(pairwise(i)):
        dist += distance[names.index(j[0])][names.index(j[1])]
    minimum = min(minimum, dist)
    maximum = max(dist, maximum)
print("min", minimum)
print("max", maximum)
