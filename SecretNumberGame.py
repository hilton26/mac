#This is the number game
import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
          print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + ', you guessed the number in ' + str(guessesTaken) + ' tries')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
print('You took ' +str(guessesTaken) + ' guesses')
