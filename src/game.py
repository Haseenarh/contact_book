import random

secret_number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break
