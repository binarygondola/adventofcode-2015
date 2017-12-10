import numpy as np

cookies = list()
nocalories = list()
values = list()
values500kcal = list()

for i in open("day15.txt").read().split("\n"):
    name, _, cap, _, dur, _, flav, _, tex, _, cal = i.split(" ")
    cap = int(cap[:-1])
    dur = int(dur[:-1])
    flav = int(flav[:-1])
    tex = int(tex[:-1])
    cal = int(cal)

    cookies.append((cap, dur, flav, tex, cal))
    nocalories.append((cap, dur, flav, tex))

a = np.array(nocalories)

r = 101
for j in range(r):
    for k in range(r - j):
        for i in range(r - j - k):
            prop = (j, k, i, r - k - i - j - 1)
            b = np.array(prop)
            cookie = np.matmul(b, a)
            if min(cookie) > 0:
                d = 1
                for q in cookie:
                    d = d * q
                values.append(d)
                # part 2
                c = 0
                for q in range(len(prop)):
                    c += prop[q] * cookies[q][4]
                if c == 500:
                    values500kcal.append(d)


print("The best cookie =", max(values))
print("The best 500 kcal cookie =", max(values500kcal))

