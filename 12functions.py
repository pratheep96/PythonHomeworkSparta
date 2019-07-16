# Function
# Run blocks of code when called
# They should be unitary / small
# They can take in arguments

# Function is like a machine
    # It can take in inputs
    # It can perform actions
    # It outputs different objects

# An argument in a function is a variable that exists only in the scope of the function
# A function needs to be called to run its code

# Syntax

#def name_function(arg1, arg2):
    # runs block of code

#Good Practices
# - functions should be unitary/ small jobs/ one job
# - arguments should have good names
# - functions should be used to keep your code DRY
    # DRY - Don't Repeat Yourself
# - functions should return NOT print

def say_hello():
    print('Hello there')

say_hello()

def full_name(f_name, l_name): #These arguments can only be used in side the block of code
    full_name_var = f_name + ' ' + l_name
    return full_name_var 

print(full_name('Hamza', 'Danielson'))