#                     basic game character system

class character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_status(self):
        print("Name : ", self.name)
        print("Health : ", self.health)

class warrior(character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
        
    def show_status(self):
        super().show_status()
        print("Weapon : ", self.weapon)

class mage(character):
    def __init__(self, name, health, magic_power):
        super().__init__(name, health)
        self.magic_power = magic_power

    def show_status(self):
        super().show_status()
        print("Magic power : ", self.magic_power)

warrior = warrior("Thor", 100, "AXE")
mage = mage("merlin", 80, 95)

warrior.show_status()
mage.show_status()