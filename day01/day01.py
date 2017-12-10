s = open('day01.txt', 'r').read()
left = 0
right = 0

for i in range(len(s)):
    if s[i] == '(':
        left += 1

    else:
        right += 1
    if left - right == -1:
        print(i)
        break
