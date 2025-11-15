import random
number = random.randint(1, 100)

print ("This is the Number Guessing Game. You have 10 chances to guess the correct number between 1 and 100.")
attempts = 10
while attempts >0:
    guess = int(input("Guess the Number: "))

    if guess > number:
        print ("lower")

    elif guess < number:
        print ("higher")

    elif guess == number:
        print ("Correct, you win!")
        break   # ends the loop

    attempts -= 1
    print ("Attempts Left:", attempts)

    if attempts == 0:
        print("Out of guesses! The number was:", number)
