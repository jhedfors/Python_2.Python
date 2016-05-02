# Assignment: Scores and Grades
# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what is the grade of that score. Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def grade(score):
    if(score >= 90):
        print "Score: %d; Your grade is A" %score
    elif(score >= 80) :
        print "Score: %d; Your grade is B" %score
    elif(score >= 70):
        print "Score: %d; Your grade is C" %score
    elif(score >= 60):
        print "Score: %d; Your grade is D" %score
    else:
        print "Score: %d; Your grade is F" %score


def prompt():
    for value in range(0,10):
        user_input = input("Enter score:")
        grade(user_input)
    print "End of program. Bye!"

prompt()
