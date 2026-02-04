import random

asci_logo = r"""
  ________                             __                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""

def GuessingGame():
    print(asci_logo)
    print("Welcome to the Guessing game!")

    number = random.randint(1, 100)
    print("I have picked a number between 1 and 100. Try to guess it!")

    level_choice = input("Choose level of difficulty(easy or hard): ")
    if level_choice == "easy":
        lives = 10
    elif level_choice == "hard":
        lives = 5
    else:
        print("Wrong input")


    while True:
        if lives == 0:
            print(f"You dont have any more lives! You lose! The number was {number}")
            break

        print(f"You have {lives} attempts left")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The number was {guess}")
            break
        elif guess < number:
            print("Too low!")
            print("Guess again")
            lives-=1
        else:
            print("Too high!")
            print("Guess again")
            lives-=1

GuessingGame()