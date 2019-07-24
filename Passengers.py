class Passenger():
    def __init__(self, name, age, passport_number, origin, destination):
        self.name = name
        self.age = age
        self.passport_number = passport_number
        self.origin = origin
        self.destination = destination

    def passenger_details(self):
        print(f"my name is {self.name} and I am {self.age} old and my passport number is {self.passport_number} "
              f"and I wanted to travel from {self.origin} to {self.destination}")

    def age(self,value):
        if value > 21 or value < 25:
            self.age = "Go to Vegas"
        else:
            self.age = "Stay at home"


william = Passenger("William", 23, "GB684949", "London", "Vegas")
william.passenger_details()
william.name = "bobby"
william.passenger_details()
william.age = 30
william.passenger_details()
william.age = 21
william.passenger_details()
print(william.age)