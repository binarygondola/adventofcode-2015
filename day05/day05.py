import re


def isNice(a):
    if str(a).find("ab") > -1:
        return False
    if str(a).find("cd") > -1:
        return False
    if str(a).find("xy") > -1:
        return False
    if str(a).find("pq") > -1:
        return False
    ca = str(a).count("a")
    ce = str(a).count("e")
    ci = str(a).count("i")
    co = str(a).count("o")
    cu = str(a).count("u")

    count = ca + ce + cu + ci + co
    if count < 3:
        return False
    pattern = re.compile(r"([a-z])\1")
    match = re.search(pattern, str(a))
    if match:
        return True
    return False


def newIsNice(a):
    pattern1 = re.compile(r"([a-z]{2}).*?\1")
    pattern2 = re.compile(r"([a-z]).\1")
    match = re.search(pattern1, str(a))
    if match:
        match2 = re.search(pattern2, str(a))
        if match2:
            return True
    return False


w = open("day05.txt").read().split('\n')

nice = 0
newNice = 0
for i in range(len(w) - 1):
    # print(w[i], isNice(w[i]), newIsNice(w[i]))
    if isNice(w[i]):
        nice += 1
    if newIsNice(w[i]):
        newNice += 1

print(nice)
print(newNice)
