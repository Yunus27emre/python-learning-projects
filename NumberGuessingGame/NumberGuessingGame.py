from random import randint

while True:
    goal=randint(1,100)
    print("You have 7 guesses.")
    for i in range(7):
        guess=int(input("Guess: "))
        if guess==goal:
            print("You got it!")
            break
        elif guess<goal:
            print("Too low.")
            print("Guess again.You have {} guesses left.".format((7-i-1)))
            continue
        elif guess>goal:
            print("Too high.")
            print("Guess again.You have {} guesses left.".format((7 - i - 1)))
            continue
    print("Goals number : {}\nThank you for playing.".format(goal))
    choose=input("Would you like to play again? (y/n): ")
    if choose=="y":
        pass
    elif choose=="n":
        break