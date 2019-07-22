# Four pillars of Object Oriented Programming
# Encapsulation
# It is considered standard or best practise to keep internal data or attributes as private
# as possible. Only a class should be able to have access to internal variables

class Person():
    def __init__(self, age, name, email, height):
        self.__height = height
        self.age = age
        self.name = name
        self.email = email

    def show_details(self):
        print(f"my name is {self.name} and I am {self.age} old and my email is {self.email} and height {self.__height}")

    def set_height(self,value):
        if value > 9 or value < 0:
            self.__height = 4.5
        else:
            self.__height = value

    def get_height(self):
        return self.__height

markson = Person(25, "Markson", "joe@done.com", 120)
# markson.show_details()
# markson.name = "filipe"
# markson.show_details()
# markson.__age = 30  #python only hides from accidental outside change not incidental
markson.show_details()
markson.set_height(200)
markson.show_details()
print(markson.get_height())
#print(markson.__height) #this will crash
#print(markson._Person__height) # This will not crash
