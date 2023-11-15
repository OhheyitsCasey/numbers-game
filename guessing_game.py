line01 = "***************************************"
line02 = "  Welcome to the Number Guessing Game"

print(line01)
print(line02)
print(line01)


def start_game():
    import random
    import statistics
    n = random.randrange(1, 100)
    tries = 1
    records = []

    print("")
    while True:
        try:
            guess = int(input("Pick a number between 1-100: "))
            if guess < n:
                print("Too low")
                tries += 1
            elif guess > n:
                print("Too high!")
                tries += 1
            elif guess == n:
                print("You guessed it right!!")
                print("It took you {} tries to guess correctly".format(tries))
                print('')
                if records and (tries < min(records)):
                    print("New high score!")
                records.append(tries)
                records.sort()
                mean = round(statistics.mean(records), 2)
                median = statistics.median(records)
                mode = statistics.mode(records)
                print(f"Mean: {mean:.2f}\nMedian: {median}\nMode: {mode}\n")
                       
                again = input("Do you want to play again (type yes or no): ")
                if again == "yes":
                    start_game()
                    break
                else:
                    print("")
                    print(f"High score: {min(records)}")
                    print("")
                    print("Thanks for playing!")
                    print("")
                    print("*** Goodbye! ***")
                    print("")
                    break
        except ValueError as err:
            print("Dont try and break the game... Pick a WHOLE NUMBER between 1-100: ")

start_game()