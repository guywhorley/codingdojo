# Phase 0: fix the typos/bugs 5 or so of them...!
# Phase 1: Comment this code!
# Phase 2: Build out the game further, make the armies attack one another!
# Phase 3: Set it up some that if a member of an army has less than 0 health remove it from the army
# Phase 4: Set up the battles so that different army types fight differently!
import random
class Human(object):
    def __init__(self, clan = None):
        self.health = 100
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3
        self.clan = clan
        print 'New Human!!! Clan: ', self.clan
    def taunt(self):
        print "You want a piece of me?"
        return self
    def attack(self,target):
        self.taunt()
        luck = round(random.random() * 100)
        attack = self.strength
        # if (self.clan):
        #     pass
        #     # future arguments to determine what to do if your clan is...
        #     # maybe this should go in to the game class..
        #     # and there is something else wrong here... but since we aren't using this if statement...
        if(luck > 50):
            if(luck * self.stealth > 150):
                print 'attacking!'
                target.health -= attack
                target.reporthealth()
                return True
            else:
                print 'attack failed'
                return False
        else:
            self.health -= self.strength
            print "attack failed"
        return False
    def reporthealth(self):
        if self.health > 0:
            print "I am not dead yet!"
        else:
            print "AAAaah you've killed me"


class Ninja(Human):
    def __init__(self, clan = 'Ninja'):
        super(Ninja, self).__init__(clan)
        self.health = 70
        self.stealth = 30

class Warrior(Human):
    def __init__(self, clan = 'Warrior'):
        super(Warrior, self).__init__(clan)
        self.health = 130
        self.strength = 30

class Wizard(Human):
    def __init__(self, clan = 'Wizard'):
        super(Wizard, self).__init__(clan)
        self.health = 50
        self.intelligence = 3


class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.armies = []

    def buildArmy(self, clan = None):
        clanMap = {"Wizard": Wizard, "Ninja": Ninja, "Warrior": Warrior}
        army = []
        if clanMap[clan]:
            for human in range(random.randint(5,6)):
                army.append(clanMap[clan]())
        else:
            for human in range(random.randint(5,6)):
                army.append(Human())
        self.armies.append(army)

game = Game()
game.buildArmy('Wizard')
game.buildArmy('Ninja')
game.buildArmy('Warrior')
print '*'*50
for val in game.armies:
	for val2 in val:
		print val2.clan
    print '***'
print len(game.armies[0]), len(game.armies[1]), len(game.armies[2]), len(game.armies)

while len(game.armies) > 1:
    i = 0
    while(i < len(game.armies)):
        target = i
        print 'Army was:', i
        while target == i:
            target = random.randint(0,len(game.armies) - 1)
        print 'Target was:', target
        for troop in game.armies[i]:
            trooptarget = random.randint(0,len(game.armies[target]) - 1)
            troop.attack(game.armies[target][trooptarget])
            if game.armies[target][trooptarget].health < 1:
                del game.armies[target][trooptarget]
                if len(game.armies[target]) < 1:
                    print 'Army ', target, ' was defeated!'
                    print '#'*50
                    del game.armies[target]
                    break
        print '*'*50
        i+=1
print 'The victorious!!!!'

for val in game.armies:
    for val2 in val:
        print val2
    print '***'
