import random

guessesTaken = 0
print('I got something for you to do yo, but first, what is your name?')

myName = input()

number = random.randint(1, 20)
print('So, ' + myName + ', I am thinking of a number between 1 and 100.')

while guessesTaken < 6:
     print('Take a guess: ') # There are four spaces in front of print.
     guess = input()
     guess = int(guess)
     guessesTaken = guessesTaken + 1

     if guess < number:
         print('Too low yo!') # There are eight spaces in front of print.

     if guess > number:
         print('Too high yo!')

     if guess == number:
         break

if guess == number:
     guessesTaken = str(guessesTaken)
     print('Kwaai, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry. The number I was thinking of was ' + number)