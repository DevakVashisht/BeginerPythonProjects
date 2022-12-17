import random

ChooseNumber = int(input("Choose a number: "))
def fun_guess(x):
    game_continue = True
    Guess = random.randint(1, x)
    while game_continue:
        user_guess = int(input(f"Guess a number between 1 and {x}\n"))
        if user_guess > Guess:
            print(f"Guess a number less than {user_guess}")
        elif user_guess < Guess:
            print(f"Guess a number greater than {user_guess}")
        elif user_guess == Guess:
            print(f"The answer was {Guess}")
            print("You won!")
            game_continue = False
            break
fun_guess(ChooseNumber)
