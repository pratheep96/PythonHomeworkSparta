from AirportInheritance import *
from AirportAbstraction import *
from Passengers import *

import pytest

# def test_passenger_passenger_name():
#     assert Bob.passenger_name == "Bob Smi"

def test_passenger_passport_number():
    assert Bob.passport_number == "GB807548"
    if  Bob.passport_number == "GB807548":
        print("well done")
    else:
        print("failed")

# def test_passenger_nationality():
#     assert Bob.nationality == "British Citizen"