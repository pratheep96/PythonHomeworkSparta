class Calculator:

    def __init__(self, addition, subtration, multiplication, division):
        self.add = addition
        self.subtract = subtraction
        self.multiply = multiplication
        self.divide = division

    def addition(first_number,second_number):
        addition = first_number + second_number
        return addition

    def subtraction(first_number,second_number):
        subtraction = first_number - second_number
        return subtraction

    def multiplication(first_number,second_number):
        multiplication = first_number * second_number
        return multiplication

    def division(first_number,second_number):
        division = first_number / second_number
        return division

addition1 = Calculator.addition(5,1)
subtraction1 = Calculator.subtraction(5,1)
multiplication1 = Calculator.multiplication(5,1)
division1 = Calculator.division(5,1)

print(addition1)
print(subtraction1)
print(multiplication1)
print(division1)