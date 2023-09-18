import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 5

    print("Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between 1 and 100.")

    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))

            if guess == secret_number:
                print(f"Congratulations! You guessed the right number; which is {secret_number}")
                break
            elif guess < secret_number:
                print("Try Again! Your guess was too low!")
            else:
                print("Try Again! Your guess was too high")

            attempts += 1

        except ValueError:
            print("Invalid input. Please enter a number")

    if attempts == max_attempts:
        print(f"Game over! The secret number was {secret_number}")

    play_again = input("Do you want to play again? (Yes/N0): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thanks for playing")

guess_the_number()
