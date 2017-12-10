santa = dict()

for q in open("day14.txt").read().split("\n"):
    deer, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _ = q.split(" ")
    santa.setdefault(deer, dict())['d'] = 0
    santa[deer]['speed'] = int(speed)
    santa[deer]['time'] = int(time)
    santa[deer]['rest'] = int(rest)
    # part 2
    santa[deer]['set'] = []
    santa[deer]['pts'] = 0

# part 1
for d in santa:
    i = 0
    while i <= 2503:
        for _ in range(santa[d]['time']):
            santa[d]['d'] += santa[d]['speed']
            i += 1
            santa[d]['set'] += santa[d]['d'],
            if i > 2503:
                break
        for _ in range(santa[d]['rest']):
            santa[d]['set'] += santa[d]['d'],
        i += santa[d]['rest']

print("max distance travelled after 2503 time =", max([santa[d]['d'] for d in santa]))

# part 2
for i in range(2503):
    arr = [santa[d]['set'][i] for d in santa]
    travelled_max = max(arr)
    for d in santa:
        santa[d]['pts'] += (1 if santa[d]['set'][i] == travelled_max else 0)

print("max pts =", max([santa[d]['pts'] for d in santa]))
