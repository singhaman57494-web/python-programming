#                               main file of game

import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.equipped_weapon = None
        self.total_damage_dealt = 0
        self.inventory = None
        self.level = 1
        self.xp = 0
        self.xp_required = 100

    def show_status(self):
        print("Name : ", self.name)
        print("Health : ", self.health)
        print("Attack Power : ", self.attack_power)
        print("Equip Weapon : ", self.equipped_weapon)

    def attack(self, target):
        if self.health <= 0:
            print("Character cannot fight!")
            return
        elif self.health > 0 and target.health > 0:
            damage = random.randint(5, self.attack_power)
            self.total_damage_dealt += damage
            while self.total_damage_dealt >= 50:
                self.inventory.potions.append("Health potion")
                self.total_damage_dealt -= 50
                print(f"{self.name} earned a health potion!")
            print(f"{self.name} total damage dealt: {self.total_damage_dealt}")
            target.health = max(0, target.health - damage)
            print(f"{self.name} Attacks {target.name} for {damage} damage!")
            if target.health <= 0:
                print(f"{target.name} has been defeated!")
                self.gain_xp(120)

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} xp!")
        print(f"current xp : {self.xp} / {self.xp_required}")
        if self.xp >= self.xp_required:
            self.level += 1
            print(f"LEVEL {self.level} unlocked!")
            self.xp -= self.xp_required
            print(f"current xp : {self.xp} / {self.xp_required}")

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        self.attack_power +=  5

    def unequip_weapon(self):
        if self.equipped_weapon is not None:
            self.attack_power -=  5
            self.equipped_weapon = None
        else:
            print("no weapon Equiped!")


class Inventory:
    def __init__(self):
        self.weapons = []
        self.potions = []
        self.items = []

    def use_potion(self, character):
        if character.health > 0:
            if self.potions:
                print(f"Health potions : {self.potions}")
                self.potions.pop()
                print(f"Health potions : {self.potions}")
                character.health = min(100, character.health + 20)
                print(f"Health restored! {character.name } Current health is {character.health}")
            else:
                print("not health potion!")
        else:
            print("character cannot use potions.")

    def show_inventory(self):
        print("Weapons : ", self.weapons)
        print("Potions : ", self.potions)
        print("Items : ", self.items)


hero = Character("Aman", 100, 20)
goblin = Character("goblin", 100, 20)

aman_inventory = Inventory()
aman_inventory.weapons.append("Iron Sword")
aman_inventory.potions.append("Health Potion")
aman_inventory.items.append("Ancient Key")
hero.inventory = aman_inventory

goblin_inventory = Inventory()
goblin_inventory.weapons.append("Iron Sword")
goblin_inventory.potions.append("Health Potion")
goblin_inventory.items.append("Ancient Key")
goblin.inventory = goblin_inventory

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
    else:
        print("Invalid option! try again.")


while True:
    if goblin.health <= 0 and hero.health > 0:
        print("YOU WIN!")
        break
    elif hero.health <= 0 and goblin.health > 0:
        print("Game Over!")
        break
    use_weapon = int(input( 
    "\n ====== WEAPON==MENU=======\n"
    "\n      1 - 3 : equip weapon \n"
    "1. Equip weapon to Aman\n"
    "2. Equip weapon to Goblin\n"
    "3. Equip weapon to both\n"
    "        4 - 8 : unequip weapon : \n"
    "4. Unequip Aman's weapon\n"
    "5. Unequip Goblin's weapon\n"
    "6. Unequip both weapons \n"
    "7. Show status both \n"
    "8. restore health \n"
    "enter the number (1 - 7) : "))
    if use_weapon == 1:
        hero.equip_weapon("Iron Sword")
        print("Aman equipped Iron Sword!")
        hero.attack(goblin)
    elif use_weapon == 2:
        goblin.equip_weapon("Iron Sword")
        print("goblin equipped Iron sword!")
        goblin.attack(hero)
    elif use_weapon == 3:
        goblin.equip_weapon("Iron Sword")
        goblin.attack(hero)
        hero.equip_weapon("Iron Sword")
        hero.attack(goblin)
        print("Aman and goblin equipped Iron Sword!")
    elif use_weapon == 4:
        hero.unequip_weapon()
        print("hero had drop his weapon ")
    elif use_weapon == 5:
        goblin.unequip_weapon()
        print("goblin had drop his weapon")
    elif use_weapon == 6:
        hero.unequip_weapon()
        print("hero had drop his weapon ")
        goblin.unequip_weapon()
        print("goblin had drop his weapon")
    elif use_weapon == 7:
        hero.show_status()
        goblin.show_status()
    elif use_weapon == 8:
        while True:
            choice = input("restore health : 1. Hero 2. goblin 3. Exit 4. show inventory \nenter the number => ")
            if choice == "1":
                aman_inventory.use_potion(hero)
            elif choice == "2":
                goblin_inventory.use_potion(goblin)
            elif choice == "3":
                print("END GAME")
                break
            elif choice == "4":
                aman_inventory.show_inventory()
                goblin_inventory.show_inventory()
                print(f"Hero Health : {hero.health} Goblin Helath : {goblin.health}")
            else:
                print("Invalid choice! try again.")
    else:
        break

