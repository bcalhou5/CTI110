# Random Number File Reader
# 07/09/17
# CTI-110 M6HW2 - Random Number File Reader
# Benjamin Calhoun

def main():

    total = 0


    try:
        infile = open('random.txt', 'r')

        

        for line in infile:
            
            amount = int(line)
            total = amount + total

        infile.close()

        print('The numbers are:',format(total))

        print('The total is:', sum(int(char) for char in line.strip()))

        print('The number of random numbers read is:', len(line))

    except:
        print('An error has occurred')

main()
