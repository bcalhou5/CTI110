# Test Average and Grade
# 06/27/17
# CTI-110 M5HW1 - Test Average and Grade
# Benjamin Calhoun

def main():
    
    print ('Please enter five test scores.')
    score1 = int(input("> "))
    score2 = int(input("> "))
    score3 = int(input("> "))
    score4 = int(input("> "))
    score5 = int(input("> "))
    
    print('Score 1:',determine_grade(score1))
    print('Score 2:',determine_grade(score2))
    print('Score 3:',determine_grade(score3))
    print('Score 4:',determine_grade(score4))
    print('Score 5:',determine_grade(score5))
    

    print('average: ',calc_average(score1, score2, score3, score4, score5))
    

def calc_average(score1, score2, score3, score4, score5):
    
    average = (score1 + score2 + score3 + score4 + score5)/5
    return average

def determine_grade(score):

    if score >= 90:
        letterGrade = 'A'
    elif 80 <= score <= 89:
        letterGrade = 'B'
    elif 70 <= score <= 79:
        letterGrade = "C"
    elif 60 <= score <= 69:
        letterGrade = "D"
    else:
        letterGrade = 'F'

    return letterGrade


main()
