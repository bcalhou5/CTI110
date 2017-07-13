# Guessing Game
# 07/09/17
# CTI-110 M5HW2 - Random Number Guessing Game
# Benjamin Calhoun

import random

def main():
    counter=1
    num=random.randint(1,100)
    while True:
        print('Guess a number between 1 and 100')
        guess=input()
        i=int(guess)
        if i == num:
            print('You Won, would you like to play again? (y=yes)')
            print('It took you',(str(counter)),'attempts')
            replay()
            break
        elif i < num:
            print('Try higher')
            counter=counter+1
        elif i > num:
            print('Try lower')
            counter=counter+1
        else:
            print('Use whole integers')

def replay():
    while True:
        retry=input('Would you like to play again? (yes or no):')
        if retry == 'yes':
            main()
        if retry == 'no':
            exit()
            

main()

