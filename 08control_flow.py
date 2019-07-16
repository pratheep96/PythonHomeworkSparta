# Control Flow - If statements
# syntax - indentation matters
# if <condition>:
    #Block of code
#else:
    #Block of code
#
# age = 16
# if age >= 70:
#     print('You can do everything but take it easy')
# elif age >= 18:
#     print('your age is above 18, you can vote')
# elif age >= 16:
#     print('You can buy the lottery and probably go to prison')
# else:
#     print('you are underage, you cannot vote')

# weather = input('Is it rainy or sunny today?').strip().lower()
#
# if weather == 'rainy':
#     print('Take an umbrella with you today')
# elif weather == 'sunny':
#     print('Wear a hat')
# else:
#     print('Stay home today')

weather1 = input('What is the weather like today?').strip().lower()
weather2 = input('Anything else?').strip().lower()

if (weather1 == 'rainy' and weather2 == 'stormy') or (weather2 == 'stormy' and weather1 == 'rainy'):
    print('Take your jacket')
elif (weather1 == 'rainy' and weather2 == 'no') or (weather1 == 'foggy' and weather2 == 'no'):
    print('Take your umbrella')
else:
    print('Your answer can not be recongnised, please try again')