#Number guessing game
import random

def guessNum():
    number = random.randint(0,9)
    number__of_attemps = 0
    max_attempts = 3
    print("You have to guess the Number betn 0-9")
    print(f"You {max_attempts} attempts to guess the Number betn 0-9")
    
    while number__of_attemps < max_attempts:
        try:
            guess = int(input("Enter Your Guess: "))
        except ValueError:
            print('ENTER Valid number')

        if guess != number:
            number__of_attemps += 1
        else:
            print(f"You guessed it right {number}")
        
        if(guess < number):
            print("Guess is less than generated num")
        if(guess > number):
            print("Guess is More than generated num")
    else:
        print("Sorry You have ran out of atempts")


guessNum()