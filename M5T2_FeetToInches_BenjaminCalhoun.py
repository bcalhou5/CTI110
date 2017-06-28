# Feet to Inches
# 06/27/17
# CTI-110 M5T2_FeetToInches 
# Benjamin Calhoun

# 1 foot = 12 inches.

# Write function named "feet_to_inches"

INCHES_PER_FOOT = 12

#main function

def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#create constants that represents numbers within a function

#Call the main function.

main()


