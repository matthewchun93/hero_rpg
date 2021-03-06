#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def __init__(self, health, power):
        super(Hero, self).__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the goblin.")

    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


class Goblin(Character):
    def __init__(self, health, power):
        super(Goblin, self).__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The goblin does {self.power} damage to you.")

    def print_status(self):
        print(f"The goblin has {self.health} health and {self.power} power.")

def main():

    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')

        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
            if not goblin.alive():
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            goblin.attack(hero)
            if not hero.alive():
                print("You are dead.")

main()
