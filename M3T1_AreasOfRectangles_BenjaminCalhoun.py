# Areas of Rectangles
# Date 06/11/17
# CTI-110 M3T1 - Areas of Rectangles
# Benjamin Calhoun

#Input the length and width of rectangle 1.
#Input the length and width of rectangle 2.
#Calculate the area of rectangle 1
#Calculate the area of rectangle 2
#If area1>area2
    #display "rectangle 1 has the greatest area."
#else if area 2>area1
    #display "rectangle 2 has the greatest area."
#else
    #display "both rectangles have the same area."

# Get the dimensions of rectangle 1.

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))
 # Get the dimensions of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Calculate the areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

#Determine white has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print ('Both have the same area.')
    
