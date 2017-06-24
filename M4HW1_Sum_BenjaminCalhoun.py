# Sum of Numbers
# 06/23/17
# CTI-110 M4HW1 - Sum of Numbers
# Benjamin Calhoun

total = 0
userNumber = float(input('Please enter the first number or a negative number to quit:')) 

while userNumber > -1:
    total = total + userNumber
    userNumber = float(input('Enter the next number or a negative number to quit:'))
    
print('The sum of all the numbers you entered is', total)
