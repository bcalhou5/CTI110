# Kilometer Converter
# 06/27/17
# CTI-110 M5T1_KilometerConverter 
# Benjamin Calhoun

#Miles = Kilometers X 0.6214

#Write a program that asks the user to enter a distance in kilo. and then converts
#that distance to miles.

#"enter a distance in kilometers"
#1. input kilometers
#2. convert kilometers to miles
#3. display miles

#Use "main function"
#go to "second function"
    #"show_miles function

conversion_factor = 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers:'))

    show_miles(kilometers)

def show_miles(km):
    miles = km * conversion_factor

    print(km, 'kilometers equals', miles, 'miles.')
    
main()
