#Here the user have to keep in mind a given number and make the computer guess the number
# until the computer finds the correct number

import random                                           #imports pre-defined random library

def guess(x):
    random_number = random.randint(1,x)                 #runs/finds a random number
    guess = 0                                           #a guess number out of range as a sample to guess a number
    while guess!= random_number:
        guess = int(input(f'Guess a number betwen 1 and {x}: '))
        if guess < random_number:
            print('Sorry guess again, too low')
        elif guess > random_number:
            print('Sorry guess again, too high')
    
    print(f'Yay, congrats, you have guessed the right number {random_number}, correctly! ')

def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)

        else:
            guess = low             #could also be high since high=low

        feedback=input(f'Is {guess} too high (H), too low (L) or correct(C)'.lower())
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed the right number, {guess} correctly!')



num = int(input('Enter the maximum limit of guessing number: '))
computer_guess(num)                   #describes the maximum range of the number

