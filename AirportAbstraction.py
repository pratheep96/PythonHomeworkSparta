from AirportInheritance import People

class Passenger(People):

    def __init__(self, name, airport_size, number_runways, staff, passengers, passenger_name, passport_number, nationality):
        super().__init__(name, airport_size, number_runways, staff, passengers)
        self.passenger_name = passenger_name
        self.passport_number = passport_number
        self.nationality = nationality

    def visa(self,bool_value):
        return bool_value

    def valid_passport(self, bool_value):
        return bool_value


Bob = Passenger("Heathrow", "4500m", 3, 3000, 175000, "Bob Smith", "GB807548", "British Citizen")

print(Bob.name)
print(Bob.airport_size)
print(Bob.number_runways)
print(Bob.staff)
print(Bob.passengers)
print(Bob.passenger_name)
print(Bob.passport_number)
print(Bob.nationality)

print(Bob.visa(True))
print(Bob.valid_passport(False))