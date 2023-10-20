import random


print("Please enter the minimum value:")
min = int(input())

print("Please enter the maximum value:")
max = int(input())

random_number = random.randint(min, max)

print(f"I am thinking of a number between {min} and {max}. Can you guess it?")
guess = int(input())

while True:
    print(f"I am thinking of a number between {min} and {max}. Can you guess it?")
    guess = int(input())
    if guess == random_number:
        print("You got it!")
        break


    if guess > random_number:
         print("Guess is too high")
    elif guess < random_number:
         print("Guess is too low")






