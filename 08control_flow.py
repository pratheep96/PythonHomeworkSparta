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

weather = input('Is it rainy or sunny today?').strip().lower()

if weather == 'rainy':
    print('Take an umbrella with you today')
elif weather == 'sunny':
    print('Wear a hat')
else:
    print('Stay home today')
