"""A number-guessing game."""

from random import randint

# Put your code here

print("Welcome Players")
print('Print your name')

from random import randint

tries = 0
number = randint(1, 100)

print('Welcome! My name is The Bot, what\'s yours?')

name = input('(type in your name)')

print(f'{name}, I\'m thinking of a number between 1 and 100.')
print('Can you guess what number is?')

while True:
    guess = input('what\'s your guess? ')

    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a number, please try again.')
        continue

    if guess < 1 and guess > 100:
        print("Remember it is a number between 1 and 100, guess again!")
        continue
    tries += 1

    if guess < number:
        print('Your guess is lower, try again')

    elif guess > number:
        print('Your guess is higher, try again')

    else:
        print(f'Well done {name}!')
        print(f'You guessed my number in {tries} tries!')
        break


