number = open("day10.txt").read()

print(number)
for i in range(50):
    idx = 0
    newnum = ""
    while idx < len(number):
        sym = number[idx]
        count = 1
        while count + idx < len(number) and sym == number[count + idx]:
            count += 1
        newnum += str(count) + sym
        idx += count
    number = newnum
print(len(number))
