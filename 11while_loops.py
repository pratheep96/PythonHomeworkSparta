import time
#While loops

# Syntax
# While <condition>
    # Block of code
    # **Optional** if <condition>
#                       break

counter = 0
while counter < 28:
    print('lets go out!')
    counter += 1
    time.sleep(0.2)

print('end')

while True:
    print('Welcome to the loop')
    word = input('Tell me a word')
    if word == 'donkeys':
        print('you cracked the code')
        break
    else:
        print('ahahahaha you fool. you will never leave')
        print('AHAHAHAHAHAH')


