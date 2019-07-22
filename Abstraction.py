# Four pillars of Object Oriented Programming
# Abstraction
# Given the user only the information needed to perform a task
# While keeping unnecessary information away

class Animal:

    def __init__(self, age, weight, species):
        self.age = age
        self.weight = weight
        self.species = species

    def can_hunt(self, value):
        return value

    def can_eat (self):
        return "yum yum"

    def sleep (self):
        return "zzzz"

class Mammal(Animal):
    def __init__(self, age, weight, species, name):
        super().__init__(age, weight, species)

    def can_speak_a_language(self, can_speak):
        return "Hello"

class Birds(Animal):
    def __init__(self, age, weight, species, name, feather_colour):
        super().__init__(age, weight, species)
        self.name = name
        self.feather_colour = feather_colour

    def can_fly (self, can_fly):
        return can_fly

class Reptiles(Animal):
    def __init__(self, age, weight, species, name, region_found):
        super().__init__(age, weight, species)
        self.name = name
        self.region_found = region_found

    def is_venomous(self, value):
        return value