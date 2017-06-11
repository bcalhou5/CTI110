# Body Mass Index
# 06/11/17
# CTI-110 M3HW2 - Body Mass Index
# Benjamin Calhoun
userWeight=int(input('Enter your weight in pounds:'))
userHeight=int(input('Enter your height in inches:'))

userBmi=((userWeight * 703) / (userHeight ** 2))

if userBmi < 18.5:
    print('A person with a BMI of', userBmi, 'is considered underweight')
elif userBmi > 25:
    print('A person with a BMI of', userBmi, 'is considered overweight')
else:
    print('A person with a BMI of', userBmi, 'is considered the optimal weight')
