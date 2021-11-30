desc = ['Magic Missile costs 53 mana. It instantly does 4 damage.',
        'Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.',
        'Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.',
        'Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.',
        'Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.']


debug = True


def mprint(string):
    if debug:
        print(string)


class Player:
    mana = 500
    hp = 50
    manasum = 0
    armor = 0


class Boss:
    f = open('day22.txt').read().splitlines()
    hp = int(f[0][-2:])
    dmg = int(f[1][-2:])


class Properties:
    shieldCounter = 0
    poisonCounter = 0
    poisondmg = 3
    rechargeCounter = 0
    rechargemana = 101


class Spell:
    def __init__(self, string):
        self.description = string
        self.cost = self.getCost(string)
        self.lasting = self.getLasting(
            string) if self.hasLasting(string) else 0
        # print('Spell costs {0}, lasts for {1}'.format(self.cost, self.lasting))
        self.name = string.split(' costs')[0]

    def getCost(self, string):
        string = string.split('mana.')[0]
        string = string.split('costs')[-1]
        string = int(string)
        return string

    def hasLasting(self, string):
        return 'effect that lasts for' in string

    def getLasting(self, string):
        string = string.split('effect that lasts for')[1]
        string = string.split('turns')[0]
        string = int(string)
        return string

    def __str__(self):
        return "Spell '{0}' costs {1} mana, lasts for {2} turns".format(self.name, self.cost, self.lasting)


class Game:
    def __init__(self):
        self.boss = Boss()
        self.player = Player()
        self.props = Properties()
        self.spells = self.prepareSpells()

    def prepareSpells(self):
        spells = []
        for idx, s in enumerate(desc):
            spells.append(Spell(s))
        return spells

    def statsBoss(self):
        mprint(
            "Boss has {0} hit points and deals {1} dmg each turn".format(self.boss.hp, self.boss.dmg))

    def statsMyself(self):
        mprint(
            "You have {0} hit points and {1} mana".format(self.player.hp, self.player.mana))

    def whatToDo(self):
        mprint("What spell do you want to use? Press a number")
        for idx, s in enumerate(desc):
            mprint("    {0}. {1}".format(idx, s))
        a = input()
        return a

    def shieldEffect(self):
        return self.props.shieldCounter != 0

    def playerTurn(self):
        mprint("It's your turn!")
        a = int(game.whatToDo())
        mprint('You choose spell number {0}!'.format(a))

    def bossTurn(self):
        mprint("It's boss' turn!")
        if(self.boss.hp <= 0):
            mprint('boss ded XD')
        else:
            dmg = self.bossAttack()
            mprint("You lose {0} hp".format(dmg))
            self.player.hp = self.player.hp - dmg
            mprint("You have {0} hp".format(self.player.hp))

    def bossAttack(self):
        t = self.boss.dmg - self.player.armor if self.shieldEffect() else self.boss.dmg
        mprint("Boss does {0} dmg to you!".format(t))
        return t

    def startTurn(self):
        if self.props.rechargeCounter >= 1:
            self.player.mana += self.props.rechargemana
        if self.props.poisonCounter >= 1:
            self.boss.hp -= self.props.poisondmg
        if self.props.shieldCounter >= 1:
            self.player.armor = 7
        else:
            self.player.armor = 0
        self.statsBoss()

    def endTurn(self):
        self.props.rechargeCounter = max(self.props.rechargeCounter - 1, 0)
        self.props.poisonCounter = max(self.props.poisonCounter - 1, 0)
        self.props.shieldCounter = max(self.props.shieldCounter - 1, 0)

    def printCounters(self):
        mprint('Recharge counter: {0}'.format(self.props.rechargeCounter))
        mprint('Poison counter: {0}'.format(self.props.poisonCounter))
        mprint('Shield counter: {0}'.format(self.props.shieldCounter))

    def canCast(self, mana):
        return self.player.mana >= mana

    def castMissile(self):
        manaCost = 53
        if(self.canCast(manaCost)):
            self.boss.hp -= 4
            self.player.mana -= manaCost
            self.statsBoss()
            self.player.manasum += manaCost

    def castDrain(self):
        manaCost = 73
        if(self.canCast(manaCost)):
            self.boss.hp -= 2
            self.player.hp += 2
            self.player.mana -= manaCost
            self.player.manasum += manaCost

    def castShield(self):
        manaCost = 113
        if(self.canCast(manaCost)):
            self.props.shieldCounter = 7
            self.player.armor = 7
            self.player.mana -= manaCost
            self.player.manasum += manaCost

    def castPoison(self):
        manaCost = 173
        if(self.canCast(manaCost)):
            self.props.poisonCounter = 7
            self.player.mana -= manaCost
            self.player.manasum += manaCost

    def castRecharge(self):
        manaCost = 229
        if(self.canCast(manaCost)):
            self.props.rechargeCounter = 6
            self.player.mana -= manaCost
            self.player.manasum += manaCost

    def cast(self, a):
        if a == 0:
            self.castMissile()
        elif a == 1:
            self.castDrain()
        elif a == 2:
            self.castShield()
        elif a == 3:
            self.castPoison()
        elif a == 4:
            self.castRecharge()
        else:
            mprint("bad number")

    def endGame(self):
        if(self.player.hp <= 0):
            print("You ded XD")
            return True
        if(self.boss.hp <= 0):
            print('boss ded XD')
            return True
        return False


manasum = 0
mprint('')
mprint('')
mprint('Welcome! You are fighting a boss!')
game = Game()
spells = game.prepareSpells()
end = False
while(not end):
    game.statsMyself()
    game.startTurn()
    a = game.whatToDo()
    game.cast(int(a))
    game.endTurn()
    game.startTurn()
    game.bossTurn()
    game.endTurn()
    end = game.endGame()

print(game.player.manasum)
