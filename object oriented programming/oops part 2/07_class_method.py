#                              class method

'''
1. a class is bound to the class & recives the class as an implicit first argument.

2. note :- static method can't access or modify class state & generally for utility.

'''
class person:
    name = "anonymous"

    def changename(self, name):
        person.name = name  # changename type 1

    #   and type 2
    def changnamee(self , name):
           self. __class__.name = "rohit"

    #  and type 3
    @classmethod
    def changeingname(cls , name):
         cls.name = name

p1 = person()

p1.changename("rahul kumar")
print(p1.name)
print(person.name)

p1.changnamee("rohit sharma")
print(p1.name)

p1.changeingname("lokesh")
print(p1.name)