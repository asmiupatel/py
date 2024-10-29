import random

index = random.randint(1, 100)

print("Guess a number between 1 and 100:")


while True:
    a = int(input())

    if a < 1 or a > 100 :
        print("Please ener a valid guess.")
    elif a == index:
        print("You guessed the correct number!")
    elif a < index :
        print("Try guessing a bit higher.")
    else :
        print("Try guessing a bit lower.")    