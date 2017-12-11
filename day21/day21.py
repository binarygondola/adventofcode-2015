class Item(object):
    def __init__(self, name, p, a, d):
        self.attack = int(a)
        self.defence = int(d)
        self.price = int(p)
        self.name = name

    def __str__(self):
        return self.name + ": " + str(self.price) + "$, " + str(self.attack) + " ATK, " + str(self.defence) + " DEF"

    def __repr__(self):
        return '\'' + str(self) + '\''


class Warrior:
    def __init__(self, name, a, d, hp):
        self.hp = hp
        self.attack = a
        self.defense = d
        self.items = []
        self.eqcost = 0
        self.name = name

    def addItem(self, item):
        self.items.append(item)
        self.attack += item.attack
        self.defense += item.defence
        self.eqcost += item.price

    def losthp(self, hp):
        self.hp -= hp
        # print(self.name + " lost " + str(hp) + " hp. Now has " + str(self.hp))

    def __repr__(self):
        return str(self)

    def __str__(self):
        s = '\n'
        if self.items:
            s = "\nHas these items:\n"
            for x in self.items:
                s += str(x) + "\n"
        return "Warrior " + self.name + ". Has " + str(self.attack) + " attack, " + str(self.defense) + " defense and "\
               + str(self.hp) + " hit points. Price of eq = " + str(self.eqcost) + s


def fight(player, enemy):
    enemy.losthp(max(1, player.attack - enemy.defense))
    player.losthp(max(1, enemy.attack - player.defense))


items = list()
for i in open("day21.txt").read().split("\n"):
    if ':' in i:
        items.append(list())
    elif ':' not in i:
        i = i.split(" ")
        i = [x for x in i if len(x) > 0]
        items[-1].append(Item(i[0], i[1], i[2], i[3]))


prices = list()
badprices = list()

for weapon in range(5):
    for armor in range(5):
        for rings in range(42):
            enemy = Warrior("Boss", 9, 2, 103)
            player = Warrior("binarygondola", 0, 0, 100)

            if rings == 0:
                pass
            elif rings <= 6:
                player.addItem(items[2][rings - 1])
            else:
                rings -= 6
                player.addItem(items[2][rings // 6])
                player.addItem(items[2][rings % 6])

            player.addItem(items[0][weapon])
            player.addItem(items[1][armor])

            while player.hp > 0 and enemy.hp > 0:
                fight(player, enemy)

            if enemy.hp <= 0:
                # print("Success " + str(player.eqcost) + " -> " + str(player.items))
                prices.append(player.eqcost)
            elif player.hp <= 0:
                # print("Failure " + str(player.eqcost) + " -> " + str(player.items))
                badprices.append(player.eqcost)

print("Part 1:", min(prices))
print("Part 2:", max(badprices))