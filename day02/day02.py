s = open('day02.txt', 'r').read().split('\n')

# papier
suma = 0
for i in range(len(s) - 1):
    inty = [int(x) for x in s[i].split('x')]
    iloczyn = 2 * (inty[0] * inty[1] + inty[0] * inty[2] + inty[2] * inty[1])
    suma += iloczyn
    suma += inty[0] * inty[1] * inty[2] / max(inty)
print(suma)

# wstążka
suma = 0
for i in range(len(s) - 1):
    inty = [int(x) for x in s[i].split('x')]
    suma += 2 * (inty[0] + inty[1] + inty[2] - max(inty))
    suma += inty[0] * inty[1] * inty[2]
print(suma)
