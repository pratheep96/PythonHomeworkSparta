from Day4.Abstraction import Reptiles

class Snake(Reptiles):

    def __init__(self, age, weight, species, name, region_found, number_of_fangs, length):
        super().__init__(age, weight, species, name, region_found)
        self.number_of_fangs = number_of_fangs
        self.length = length

    def can_constrict(self,bool_value):
        return bool_value

    def can_swim(self, bool_value):
        return bool_value


python = Snake (35, 450,"pythoras", "Bop", "Moorgate", 0, 12)

print(python.age)
print(python.weight)
print(python.species)
print(python.name)
print(python.region_found)
print(python.number_of_fangs)
print(python.length)

print(python.can_constrict(True))
print(python.can_swim(True))