import random
def playgame():
    attempts = 0
    print("======================================")
    print(" Welcome to the Number Guessing Game!  ")
    print("======================================")
    number = random.randint(1, 100)
    user_number = 0
    while user_number != number:
         user_number = int(input("Guess a number between 1 and 100: "))
         attempts += 1
         if user_number == number:
             print("congratulations! You guessed the correct number!")
             print(f"it took you {attempts} attempts to guess the number.")
             break
         elif user_number < 1 or user_number > 100:
             print("Invalid input! Please enter a number between 1 and 100.")
         elif user_number > number:
             print("Nice try! but the number is lower than your guess.")
         elif user_number < number:
             print("Nice try! but the number is higher than your guess.")
playgame()
while True:
     choice = input("Do you want to play again? (yes/no): ").lower()
     if choice != "yes" and choice != "no":
            print("Invalid input! Please enter 'yes' or 'no'.")
     elif choice == "yes":
         playgame()
         
     elif choice == "no":
         print("---------------------------------")
         print("       Thanks for playing         ")
         print("---------------------------------")
         break