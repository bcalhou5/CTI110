# Random Number File Write
# 07/09/17
# CTI-110 M6HW1 - Random Number File Writer
# Benjamin Calhoun

#Write a program that writes a series of random numbers to each file.
#Each random number should be in the range of 1 through 500.
#The application should let the user specify how many random numbers
#the file will hold.

import random

random_file = open('random.txt', 'w')

for i in range(int(input('How many random numbers?:'))):
    line=str(random.randint(1,500))
    random_file.write(line)
    print(line)

random_file.close()

print('\nReading the file.')
random_file=open('random.txt', 'r')
print(random_file.read())
random_file.close()
