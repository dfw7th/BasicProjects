# Import the random library to generate random numbers
import random

# We create a basic error handling feature for our number game
try:
    # Generating the random number
    number = random.randint(1, 10)
    # Assigning GUESS to a random string so we can initially
    # use it in our while loop
    GUESS = " "
    # This loop iterates while our number is not equal to the GUESS
    # The loop is iterated until false
    while number != GUESS:
        # Taking user input and Assigning "GUESS" to a user input
        GUESS = int(input("Pick a number from 1 to 10: "))
        if GUESS == number:
            print("You got the number, good job dawg")
        else:
            print("Try again Fam")
except ValueError:
    print("That's a letter or symbol bruv")
