# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026


# Multiplication Table
print("===========Times Table==========")

# Get a number from the user
num = int(input("Enter a number: "))

# Print the multiplication table from 1 to 10
for i in range(1,11):
    print(f"{num} X {i} = {i *num}")

print("================================")


# ATM PIN Check
print("==========ATM PIN Check=========")

# Set the correct password and initialize counters
possword = 4321
count = 0
tries = 3

# Allow the user up to three attempts
while count<3 :

    # Ask the user to enter the password
    user = int(input("Enter possoword: "))

    # Check whether the entered password is correct
    if user == possword:
        print("Welcome!")
        break

    # Handle an incorrect password
    elif user != possword:
        print("Wrong possoword!!")

        # Increase wrong attempts and decrease remaining tries
        count+=1
        tries -=1
        print(f"you have {tries} trie left")

    # Block the card after three wrong attempts
    if count == 3:
        print("your card has been Blocked!") 
        break         

print("==================================")


# Number Guessing Game
print("=========== Number Guessing Game ===========")

# Import random module to generate a random number
import random

# Keep the game running until the user chooses to exit
while True:

    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    guess_count = 0

    # Allow the user to guess until the correct number is found
    while True:

        # Get the user's guess
        guess = int(input("Guess a number between 1 and 50: "))

        # Count each guessing attempt
        guess_count += 1

        # Check if the guess is lower than the secret number
        if guess < secret_number:
            print("Too low!")

        # Check if the guess is higher than the secret number
        elif guess > secret_number:
            print("Too high!")

        # If neither condition is true, the guess is correct
        else:
            print(f"Correct! You got it in {guess_count} attempts.")
            break

    # Ask the user whether they want to play again
    play_again = input("Want to play again? (y/n): ").lower()

    # End the game if the user enters n
    if play_again == "n":
        print("Thank you for playing!")
        break

    # Start a new game if the user enters y
    elif play_again == "y":
        print("Starting a new game...")

    # End the game if the user enters an invalid choice
    else:
        print("Invalid choice. Game will end.")
        break


print("===========================================")