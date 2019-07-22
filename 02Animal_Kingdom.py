# class Animal:
#
#     animal_kind = "I dont know"
#
#     def speak():    #this is inside a class hence it is a method
#         return "what ??????"

# def speak2(self): #this however is not inside the class it is in the file itself hence is now called a function
#     return "what ??????"

#When a function is put inside a class, it is no longer a function but a method

# print(Animal.speak()) #Why did this fail
# print(Animal.animal_kind) # Why did this pass

# dog = Animal() # now I have an object of type animal
# dog2 = Animal() # new animal
# print(dog.animal_kind)
# print(dog2.animal_kind)
# dog2.animal_kind = "woof"
# print(dog.animal_kind)
# print(dog2.animal_kind)
# #difference with the self key word
# print(Animal.speak())
# print(dog.speak())

# class Animal:
#
#     animal_kind = "cow"
#
#     def speak(self):
#         return "what ????"
#
#     def eat(self):
#         return "yummy"
#
#     def speak2():
#         return "hello"
#
# dog = Animal() #now i have an object of type animal
# cat = Animal() #new animal

#how does dog relate to members
#how object relate with class members
# print(dog.speak()) # object dog know this because of having self
# print(dog.speak2()) # object dog does not know this because of not having self
# print(dog.eat())
# print(Animal.speak()) #Animal does now know this because it has self
# print(Animal.speak2()) # Animal know this because it does not have self

# print(dog1.animal_kind)
# dog1.animal_kind = "I am a dog"
# print(dog1.animal_kind)
# print(Animal.animal_kind)
# Animal.animal_kind = "mouse"
# print(dog1.animal_kind)
# dog3 = Animal()
# #using objects
# print(dog3.animal_kind)
# print(dog3.speak())
# #using class
# print(Animal.animal_kind)
# print(Animal.speak())

class Furniture:

    size = "large"

    def moving_home(self):
        return "pack it up"

    def shop():
        return "new bed"

sofa = Furniture()
bed = Furniture()

print(sofa.size)
print(sofa.moving_home())
print(Furniture.shop())

bed.size = "King size"
print(bed.size)