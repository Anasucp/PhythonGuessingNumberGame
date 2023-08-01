import random

print("Number Guessing Game")

while True:
    system_number = random.randint(0, 20)

    while True:
        user_guess = input("Guess the number (0-20): ")
        
        
        if user_guess == system_number:
        	print("You guessed the correct number.")
        	break
        else:
            print("Try again.")
            print("Actual answer is:")
            print(system_number)
            break

    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        print("Thanks for playing.")
        break
