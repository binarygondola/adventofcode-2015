w = open('day03.txt', 'r')
w = w.read()

t = []
x, y = 0, 0
xr, yr = 0, 0
t += (x, y),
for i in range(0, len(w), 2):
    if w[i] == '^':
        y += 1
    if w[i] == 'v':
        y -= 1
    if w[i] == '>':
        x += 1
    if w[i] == '<':
        x -= 1
    if not (x, y) in t:
        t += (x, y),
    # robbo santa

    i += 1

    if i >= len(w):
        break
    if w[i] == '^':
        yr += 1
    if w[i] == 'v':
        yr -= 1
    if w[i] == '>':
        xr += 1
    if w[i] == '<':
        xr -= 1
    if not (xr, yr) in t:
        t += (xr, yr),

    print(xr, yr, 'asd', x, y, '---', i)

print(len(t))
