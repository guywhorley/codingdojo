# Odd/Even Assigment
# Guy Whorley
# Count from 1 to 2000. Display each number and specify whether it is odd or even.
# 05/02/2015 - gcw - created file

# process numbers from 1 to 2001
def isEvenOdd():
    for i in range(1, 2001):
        numType = ""
        if (i%2 == 0):
            numType = "even"
        else:
            numType = "odd"
            # print out info on current iteration
        print "Number {} is {}.".format(i, numType)
#end def

isEvenOdd()
