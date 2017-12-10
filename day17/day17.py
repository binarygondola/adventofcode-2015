def search(s, num):
    if sum(s) == 150:
        # part 2
        combinations.append(len(s))
        return 1
    if sum(s) > 150:
        return 0
    added = 0
    for i in range(len(num)):
        s.append(num[i])
        added += search(s, num[i+1:])
        s.remove(num[i])
    return added


combinations = list()

containers = list(int(i) for i in open("day17.txt").read().split("\n"))
containers.sort()

s = search(list(), containers)

print(s)
# part 2
print(combinations.count(min(combinations)))
