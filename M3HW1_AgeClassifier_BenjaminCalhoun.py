
# Age Classifier
# 06/11/17
# CTI-110 M3HW1 - Age Classifier
# Benjamin Calhoun

infant = 1
child = 12
teenager = 19
adult = 20

age=int(input('Enter your age:'))
if age <=infant:
    print('You are an infant')
else:
    if age <= child:
        print('You are a child')
    else:
        if age <=teenager:
            print('You are a teenager')
        else:
            print('You are an adult')
            
