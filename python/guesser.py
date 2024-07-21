# This is a number guesser game
import random
print ('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,20)
print ('Thank you, ' +name+ '. Guess  the number of times I have queued up at ausländerbehörde?')


for guessesTaken in range(1,5):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Too low. Take it up a notch')
    elif guess > secretNumber:
        print('Ok. A bit too high. Its not that crazy \U0001F923')
    else:
        break #When user guesses correctly
if guess ==secretNumber:
    print('Great! Now you understand me. \U0001F923')
else:
    print ('Nope. The numeber is ' + str(secretNumber))