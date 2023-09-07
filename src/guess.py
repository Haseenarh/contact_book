from emoji import emojize

import random
random_number = random.randint(1,100)
turns = 0
while True: 
     guess = input("Enter a number between 1 and 100: :😏:")
     turns += 1
    
    
     try:
         guess = int(guess)
     except ValueError:
         print(emojize(":🫠: That's not a valid number. Please try again. :🤦‍♀️🤪:"))
         continue


     if random_number == guess:
         print(emojize(":🏆: Congratulations, You won! :🏆👏:"))
         print("Number of turns you have used: ", turns)
         break
     elif random_number > guess:
         print(emojize(":⬆: Your guess was low, please enter a higher number"))
     else:
         print(emojize(":⬇: Your guess was high, please enter a lower number"))
