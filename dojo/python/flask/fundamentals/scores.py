# Scores and Grades
# Guy Whorley
# Prompt user 10x for a test score between 60 and 100. Display the grade and score.
# 05/02/2016 - gcw - created

def gatherScores():
    grade = ""
    print "\n" * 25
    # prompt user for 10 scores
    for i in range(1,11):
        grade = ""
        score = input("Please enter a score between 60 and 100: ")
        if (score < 60 or score > 100):
            print "*** Please enter a valid score between 0 - 100 ***"
        else:
            if (score >= 90):
                grade = "A"
            elif (score >= 80):
                grade = "B"
            elif (score >= 70):
                grade = "C"
            elif (score >=60):
                grade = "D"
            print "Your grade is {}".format(grade)
#end def

gatherScores()
print "\nEnd of program. Bye!"
