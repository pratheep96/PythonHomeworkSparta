def additions(first_number,second_number):
    First_number: int(input("Enter your first number"));
    Second_number: int(input("Enter your second number"))
    additions_var = 'Your total is' + first_number + second_number
    return additions_var

def subtraction(first_number,second_number):
    First_number: int(input("Enter your first number"));
    Second_number: int(input("Enter your second number"))
    subtraction_var = 'Your total is' + first_number - second_number
    return subtraction_var

def multiplication(first_number,second_number):
    First_number: int(input("Enter your first number"));
    Second_number: int(input("Enter your second number"))
    multiplication_var = 'Your total is' + first_number * second_number
    return multiplication_var

def division(first_number,second_number):
    First_number: int(input("Enter your first number"));
    Second_number: int(input("Enter your second number"))
    division_var = 'Your total is' + first_number / second_number
    return division_var

import math

def area_of_circle(radius):
    area_of_circle = radius**2 * math.pi
    return area_of_circle

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("You are "+ str(h_cm) + "cm")