# Four pillars of Object Oriented Programming
# Inheritance

class Vehicle:

    def __init__(self, make, colour, engine_size, year, speed):
        self.make = make
        self.colour = colour
        self.engine_size = engine_size
        self.year = year
        self.speed = speed
    def start(self):
        return "vroom vroom"
    def stop(self):
        return "screech"
    def accelerate(self):
        return self.speed++10
    def horn(self):
        return "beep beep"


class Truck(Vehicle):

    def __init__(self, make, colour, engine_size, year, speed, trailer_size):
        super().__init__(make, colour, engine_size, year, speed)
        self.trailer_size = trailer_size

class Boat(Vehicle):

    def __init__(self, make, colour, engine_size, year, speed, sail, deck):
        super().__init__(make, colour, engine_size, year, speed)
        self.sail = sail
        self.deck = deck
    def sink(self):
        return "help me im dying"
    def stop(self):
        return "splash"

my_car = Vehicle("Honda", "Red", 1.6, 1995, 20)     #Constructor method / initialization of car instance
my_truck = Truck("Ford", "Silver", 7.5, 2019, 14, 10)
my_boat = Boat("Yamaha", "White", 25, 1875, 30, "Headsail", "Orlop")

print(my_boat.start())
print(my_boat.accelerate())
print(my_boat.stop())
print(my_boat.horn())
print(my_boat.sink())

print(f"Daniel has a {my_car.make} of size {my_car.engine_size} of colour {my_car.colour} and is from {my_car.year}")
print(f"Omid has a {my_truck.make} of size {my_truck.engine_size} of colour {my_truck.colour} and is from {my_truck.year} "
     f"and its trailer size is {my_truck.trailer_size} inches long")
print(f"Zaid has a {my_boat.make} of size {my_boat.engine_size} of colour {my_boat.colour} and is from {my_boat.year} "
      f"and it has a {my_boat.sail} and an {my_boat.deck} deck")