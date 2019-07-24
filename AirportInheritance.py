class Airport:

    def __init__(self, name, airport_size, number_runways):
        self.name = name
        self.airport_size = airport_size
        self.number_runways = number_runways
    def start(self):
        return "go to boarding area"
    def baggagearea(self):
        return "bring your bags to the baggage area"


class People(Airport):

    def __init__(self, name, airport_size, number_runways, staff, passengers):
        super().__init__(name, airport_size, number_runways,)
        self.staff = staff
        self.passengers = passengers
    def passport_use(self):
        return "show us your passport"

class Aircraft(Airport):

    def __init__(self, name, airport_size, number_runways, plane_number, company):
        super().__init__(name, airport_size, number_runways)
        self.plane_number = plane_number
        self.company = company
    def boarding(self):
        return "time to board the flight"

my_airport = Airport("Heathrow", "2500m", 5)     #Constructor method / initialization of car instance
my_people = People("Gatwick", "1400m", 3, 300, 125000)
my_aircraft = Aircraft("Luton", "1800m", 1, "BA7489", "British Airways")

print(my_airport.start())
print(my_airport.baggagearea())
print(my_people.passport_use())
print(my_aircraft.boarding())

print(f"Daniel owns {my_aircraft.name} airport of size {my_aircraft.airport_size} with {my_airport.number_runways} runways")
