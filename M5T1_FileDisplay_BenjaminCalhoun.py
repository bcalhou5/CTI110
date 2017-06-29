# File Display
# 06/28/17
# CTI-110 M5T1 - File Display
# Benjamin Calhoun

#open the file
#for each line in the file:
    #read the line and display it
#close the file

myfile = open('numbers.txt', 'r')

# read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

#close the file.

myfile.close()
