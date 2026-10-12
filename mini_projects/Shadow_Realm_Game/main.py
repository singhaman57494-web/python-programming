#                               main file of game

import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def show_status(self):
        print("Name : ", self.name)
        print("Health : ", self.health)
        print("Attack Power : ", self.attack_power)

    def attack(self, target):
        if self.health <= 0:
            print("Character cannot fight!")
            return
        elif self.health > 0 and target.health > 0:
            damage = random.randint(5, self.attack_power)
            target.health = max(0, target.health - damage)
            print(f"{self.name} Attacks {target.name} for {damage} damage!")
            if target.health <= 0:
                print(f"{target.name} has been defeated!")


hero = Character("Aman", 100, 20)
goblin = Character("goblin", 100, 10)

while goblin.health > 0 and hero.health > 0:
    print("1. Attack")
    print("2. check status")
    print("3. Run Away")
    option = int(input("choose a number(1-3) : "))
    if option == 1:
        hero.attack(goblin)

        if goblin.health > 0 and hero.health > 0:
            goblin.attack(hero)
    elif option == 2:
        goblin.show_status()
        hero.show_status()
    elif option == 3:
        break

if goblin.health <= 0 and hero.health > 0:
    print("YOU WIN!")
elif hero.health <= 0 and goblin.health > 0:
    print("Game Over!")


class Inventory:
    def __init__(self):
        self.weapons = []
        self.potions = []
        self.items = []

    def use_potion(self, character):
        if self.potions:
            print("potion available!")
            self.potions.pop()
            character.health = min(100, character.health + 20)
            print("Health restored! Current health : ", character.health)
        else:
            print("not available!")


    def show_inventory(self):
        print("Weapons : ", self.weapons)
        print("Potions : ", self.potions)
        print("Items : ", self.items)

inventory = Inventory()

inventory.use_potion(hero)
inventory.use_potion(hero)

inventory.weapons.append("Iron Sword")
inventory.potions.append("Health Potion")
inventory.items.append("Ancient Key")
inventory.show_inventory()
