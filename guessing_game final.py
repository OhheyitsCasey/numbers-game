line01 = "***************************************"
line02 = "  Welcome to the Number Guessing Game"

print(line01)
print(line02)
print(line01)


def start_game():
    import random
    n = random.randrange(1, 10)
    tries = 1

    print("")
    while True:
        try:
            guess = int(input("Pick a number between 1-10: "))
            if guess < n:
                print("Too low")
                tries += 1
            elif guess > n:
                print("Too high!")
                tries += 1
            elif guess == n:
                print("you guessed it right!!")
                print("It took you {} tries to guess correctly".format(tries))
                print('')
                again = input("Do you want to play again (type yes or no): ")
                if again == "yes":
                    start_game()
                    break
                else:
                    print("Thanks for playing!")
                    print("Goodbye!")
                    break
        except ValueError as err:
            print("Dont try and break the game... Pick a WHOLE NUMBER between 1-10: ")
start_game()