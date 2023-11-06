
line01= "***************************************"
line02= "  Welcome to the Number Guessing Game"

print(line01)
print(line02)
print(line01)

def start_game():
    import random
    n = random.randrange(1,10)
    tries = 1

    print("")
    while True:
        try:
            guess = int(input("Pick a number between 1-10: "))
            while n!= guess:
                if guess < n:
                    print("Too low")
                    guess = int(input("Guess Again: "))
                    tries +=1
                elif guess > n:
                    print("Too high!")
                    guess = int(input("Guess Again: "))
                    tries +=1
        except ValueError as err:
            print("Dont try and break the game... Pick a WHOLE NUMBER between 1-10: ")

            print("you guessed it right!!")
            print("It took you {} tries to guess correctly".format(tries))
            print('')            

            again = input("Do you want to play again (type yes or no): ")
            if again == "yes":
                start_game()
            else:
                print("Thanks for playing!")
                print("Goodbye!")
                SystemExit

start_game()