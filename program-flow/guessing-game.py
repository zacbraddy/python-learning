import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        break

    if guess < answer:
        print("Too low bud")
    elif guess > answer:
        print("The guess is too damn high!")

    print("Try again there, champ?")
    guess = int(input())

if guess != answer:
    print("OMG you couldn't guess it you loser!!")
else:
    print("...first time")
