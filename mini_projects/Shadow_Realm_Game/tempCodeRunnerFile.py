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