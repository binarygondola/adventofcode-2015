import hashlib

h = hashlib.md5()

i = 0
while True:
    s = str(i)
    s = "iwrupvqb" + s
    h.update(s.encode('utf-8'))
    d = h.hexdigest()
    if d[0] == '0' and d[1] == '0' and d[2] == '0' and d[3] == '0' and d[4] == '0' and d[5] == '0':
        print(s, d)
        break
    i += 1
    h = hashlib.md5()
print(i)
