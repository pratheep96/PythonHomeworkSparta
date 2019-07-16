#CHAPTER ONE
print("You are Ollie, a likeable young guy in search of love. Our story begins when Ollie comes across an attractive young woman on Tinder...");

swipe_choice = input("Will you swipe left or right?: (1)Right (2)Left").lower().strip()

if swipe_choice == 'right' or swipe_choice == '1':
    print("She swiped right, too! It's a match! Now don't screw this up .....");
elif swipe_choice == 'left' or swipe_choice == '2':
    print("Hmm, perhaps Ollie's standards are a little high ... GAME OVER")

#CHAPTER TWO
print("She messages you and asks for a date! But she wants you to pick the type of restaurant.");

food_choice = input("What kind of food will you choose?: (1)Italian (2)Curry (3)Pub grub");

if food_choice == 'italian' or food_choice == '1':
    print("AH, molto bella");
elif food_choice == 'curry' or food_choice == '2':
    print("Curry on a first date!? What were you thinking? GAME OVER")
elif food_choice == 'pub grub' or food_choice == '3':
    print("Lovely jubbly")
else:
    print("You have bad taste of food, good bye!")

# CHAPTER THREE

drunk_guess = input("You meet at the restaurant and after an hour, everything seems to be going fine! However, you notice your date might have had a bit much to drink... what do you think? (Enter true or false)");

print("Whatever you say! Oh no, now she's asking how old you think she is! Maybe she's had too much drink to really notice what you say...")

age_guess = input("What age will you say?");

if age_guess < '30' or drunk_guess == 'true':
    print("She smiles and shrugs. 'I'll never tell!' Phew, that was a close one!")
else:
    print("Uh, I think you might have miscalculated somewhere... GAME OVER")

# CHAPTER FOUR
print("The rest of the evening goes wonderfully and soon, the bill arrives. Yikes! £100!?")

pay_choice = input("What will you do?: (1)Say you left your wallet at home. (2)Offer to pay.");
# var
# money_in_wallet = parseInt(prompt("Wait... how much money do you actually have?"));
#
# // Write
# an if / else statement
# including
# the and operator - if your
# pay_choice is to
# Offer
# to
# pay
# AND
# the
# money_in_wallet is over or equal
# to
# 100, execute
# the
# first
# alert, but if EITHER
# of
# those
# conditions
# isn
# 't met, execute the second with the throw
#
# alert("How very gallant of you! She seems impressed...")
#
# alert("Sorry, nobody likes a cheapskate.")
# throw
# "Don'tBeSoTightError";