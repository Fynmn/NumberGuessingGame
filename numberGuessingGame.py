import random
import time

number = random.randrange(0, 100)

print("\n\tWelcome to Number Guessing Game, player!")
time.sleep(2)
player_name = input("\nWhat is your name, player? ")
print("Okay " + player_name + " let's play!")
time.sleep(1)

def guesser():
    global number
    guess = int(input("Guess the number: "))
    while number != guess:
        if (guess == number):
            print("Wow, you got it!")
        elif (guess > number):
            print("Try again with a lower number")
            guess = int(input("Guess the number: "))
        elif (guess < number):
            print("Try again with a higher number")
            guess = int(input("Guess the number: "))

start_time = time.time()
guesser()
elapsed_time = time.time() - start_time


print("\nThe number is " + str(number) + "," + " Congrats " + player_name.upper() + " you got it right!")
print("You finished the Game in " + (str(elapsed_time)) + " seconds")
