from PIL import Image

conway = list()
tmp = list()
for i in range(102):
    tmp.append((0, 0))
conway.append(tmp)

for i in open("day18.txt").read().split("\n"):
    tmp = list()
    tmp.append((0, 0))
    for j in i:
        if j == '.':
            tmp.append((0, 0))
        else:
            tmp.append((1, 0))
    tmp.append((0, 0))
    conway.append(tmp)

tmp = list()
for i in range(102):
    tmp.append((0, 0))
conway.append(tmp)

con = 100

# for part 2 i lit the 4 corners
# conway[1][1] = (1, 0)
# conway[1][100] = (1, 0)
# conway[100][100] = (1, 0)
# conway[100][1] = (1, 0)

for q in range(100):
    for i in range(con):
        for j in range(con):
            add = 0
            x = i + 1
            y = j + 1
            for w in range(3):
                add += conway[x - 1][y + w - 1][0]
                add += conway[x + 1][y + w - 1][0]
            add += conway[x][y - 1][0]
            add += conway[x][y + 1][0]
            if add == 3:
                conway[x][y] = (conway[x][y][0], 1)
            if add == 2:
                conway[x][y] = (conway[x][y][0], conway[x][y][0])
    for i in range(con):
        for j in range(con):
            x = i + 1
            y = j + 1
            conway[x][y] = (conway[x][y][1], 0)

    # visualisation
    # img = Image.new('1', (100, 100))
    # img.putdata([conway[x+1][y][0] for x in range(100) for y in range(100)])
    # img.save('img'+str(q)+'.png')

    # for part 2 i lit the 4 corners
    # conway[1][1] = (1, 0)
    # conway[1][100] = (1, 0)
    # conway[100][100] = (1, 0)
    # conway[100][1] = (1, 0)

add = 0
for i in range(con):
    for j in range(con):
        add += conway[i + 1][j + 1][0]

print(add)
