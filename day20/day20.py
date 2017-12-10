number = int(open("day20.txt").read()) / 10

print(number)

houses = list()

num = 800000

for i in range(num):
    houses.append(0)

for q in range(1, num):
    for i in range(q, num, q):
        houses[i] += q
    if houses[q] > number:
        print("The house no", q, "has more presents than the input number (", houses[q], ">", number, ")")
        break

# part 2

houses = list()

num = 4000000

number *= 10

out = list()

for i in range(num):
    houses.append(0)

for q in range(1, num, 1):
    for i in range(q, q * 50, q):
        if i >= num:
            break
        houses[i] += q * 11
    if houses[q] > number:
        print("The house no", q, "has more presents than the input number (", houses[q], ">", number, ")")
        break
