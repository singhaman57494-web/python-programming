#                                       game player system

class player:
    def __init__(self, name , health):
        self.name = name
        self.__health = health

    def show_health(self):
        print("current Health : ", self.__health)

    def take_damage(self, damage):
        self.__health = max(0, self.__health - damage)

    def heal(self, amount):
        self.__health += amount

player1 = player("Rohan", 100)

player1.take_damage(30)
player1.show_health()

player1.heal(20)
player1.show_health()

player1.take_damage(200)
player1.show_health()
