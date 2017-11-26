# M6HW2_Shilke.py
# Number Guessing Game
# 12 Nov 2017


    
import random
numberofguesses = 0
secret_number = random.randint(1,100)


while numberofguesses < 10:
    number = int(input("Guess a number between 1-100 to play the game? "))
    guess = input()
    guess = int(guess)

    numberofguesses + numberofguesses + 1
    if guess < number:
        print("Your guess is to low!")
    if guess > number:
        print("Your guess is to high!")
    if guess == number:
        break
if guess == number:
    numberofguesses = str(numberofguesses)
    print("Great Job,you guessed the number in: " , numberofguesses)

if guess != number:
    number = str(number)
    print("Wrong,the number was: " ,number)

# call the main() function

