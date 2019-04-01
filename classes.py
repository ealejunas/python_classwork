# class Dog:
#
#     animal_variety = "canine"  # class variable
#
#     def __init__(self, name, color):    # running this initialise method
#         self.name = name
#         self.color = color
#
#     def bark(self):               # instance method
#         return "woof"
#
# print(Dog.animal_variety)
# print(Dog.bark)
#
# rolo = Dog("Rolo", "brown")   # running the constructor function self is rolo
# sandy = Dog("Sandy", "sandy-colored")        # self is sandy
#
# print(sandy.color)
# print(rolo.color)
# print(rolo.name)


# print(rolo.animal_variety)
# print(sandy.bark())
# print(type(rolo))
#
# sandy.animal_variety = "feline"
# print(sandy.animal_variety)


# example of rhino

class Rhino:
    def __init__(self, name, horn, size):
        self.name = name
        self.horn = horn
        self.size = size

ryan = Rhino("Ryan the Rhinosorous", True, "Massive")
bryan = Rhino("Bryan", False, "Tiny")

print(bryan.size)
print(bryan.name)

