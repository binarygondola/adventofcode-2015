import itertools
import re


def add(s):
    char = s[-1]
    if char == 'z':
        char = 'a'
        s = add(s[:-1]) + char
        return s
    char = chr(ord(char) + 1)
    s = s[:-1] + char
    return s


def threes(s):
    a, b, c = itertools.tee(s, 3)
    next(c, None)
    next(c, None)
    next(b, None)
    return zip(a, b, c)


def check(c3):
    if ord(c3[0]) == ord(c3[1]) - 1 and ord(c3[1]) == ord(c3[2]) - 1:
        return True
    return False


passwd = open("day11.txt").read()

for i in range(600000):
    tmp = 0
    passwd = add(passwd)
    for j in list(threes(list(passwd))):
        tmp += 1 if check(j) else 0

    for q in ('i', 'l', 'o'):
        tmp -= 1 if q in passwd else 0

    regex = re.compile(r"(.)\1")
    match = regex.search(passwd)
    match2 = regex.search(passwd[::-1])
    if match and match2 and tmp == 1 and match.group(1) != match2.group(1):
        print(passwd)
        input()
