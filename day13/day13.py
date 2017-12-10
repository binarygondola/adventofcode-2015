import itertools as it


def pairwise(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


people = set()
happiness = dict()
for i in open("day13.txt"):
    person1, _, what, amount, _, _, _, _, _, _, person2 = i.split()

    person2 = person2[:-1]

    amount = int(amount)*-1 if what == 'lose' else int(amount)

    people.add(person1)
    people.add(person2)

    happiness.setdefault(person1, dict())[person2] = amount

unhappy = 100000
happy = 0
for q in it.permutations(people):
    tmp = happiness[q[-1]][q[0]]
    tmp += happiness[q[0]][q[-1]]
    for pa, ir in pairwise(q):
        tmp += happiness[pa][ir]
        tmp += happiness[ir][pa]

    print(q) if tmp > happy else None

    unhappy = min(unhappy, tmp)
    happy = max(happy, tmp)

print(happy, unhappy)
