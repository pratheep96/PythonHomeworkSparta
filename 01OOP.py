# Definition/Declaration
# Invocation

class Calculator():

    def add(number_1,number_2):
        return number_1 + number_2

    def subtract(number_1,number_2):
        return number_1 - number_2

    def multiply(number_1,number_2):
        return number_1 * number_2

    def divide(number_1,number_2):
        return number_1 / number_2

    value1 = int(input("Enter first value"))
    value2 = int(input("Enter second value"))
    result = (add(value1,value2))
    print("The answer is ",result)

def AreaOfCircle(radius):
    PI = 3.142 # PI is a local variable
    area = PI * radius * radius
    return area
result = AreaOfCircle(int(input("Please enter the radius")))
print(result)


# value2 = 6 - 5
# print(value2)
#
# value3 = 7 // 2
# print(value3)
#
# value4 = 8 + 8
# print(value4)