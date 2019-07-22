# def speak(Animal):
#     return Animal.speak

# class Dog:
#     animal_kind = "canine"
#
#     def __init__(self,obj_name = "Jimmy"):
#         self.name = obj_name
#
#     def speak(self):
#         return "woof"
#
# dog1 = Dog("")
# dog2 = Dog("Jack")
#
# print(dog1.name)
# print(dog2.name)
# print(__name__)
# print(Dog.__name__)

class Dog:
    animal_kind = "chihuaha"

    #class constructor with parameters to create object
    #you dont call it directly, it is called by the python interpreter when you do Dog("value")
    def __init__(self,obj_name, collar_colour, dog_age, size):
        self.name = obj_name
        self.colour = collar_colour
        self.age = dog_age
        self.size = size

    def speak(self):
        return "woof"

dog1 = Dog("Jackson", "blue", "4", "large")

print(dog1.name, dog1.colour, dog1.age, dog1.size)
