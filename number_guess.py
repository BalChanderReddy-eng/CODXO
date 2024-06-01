import random

##setting the lower number
lower = 0
#setting the high number
upper = 10
##number of attempts user can do
max_attempts = 3


##checking for attempts
def play_game():
    ##this generats the number between lower and upper
    sec_number = random.randint(lower, upper)
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        print(f"attempt {attempts}/{max_attempts}")

        ###taking input from the user
        user_guess = int(input("enter number to guess: "))

        ##checking if the user has guessed the correct number
        if (user_guess == sec_number):
            print("Hoorey both are same")
            won = True
            break
        else:
            print("wrong number")

        ##if user not won
        if not won:
            print(f"you have guessed the wrong number! the secret number is ,{sec_number}")



while True:
    play_game()
    play_again = input("want to play again? (yes/no)").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break



