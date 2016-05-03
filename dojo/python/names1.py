# Names Part I
# Guy Whorley
# Create a program that manipulates dictionaries
# 05/02/2016 - gcw - created

students = [
    { 'fname' : 'Michael', 'lname' : 'Jordan'  },
    { 'fname' : 'John'   , 'lname' : 'Rosales' },
    { 'fname' : 'Mark'   , 'lname' : 'Guillen' },
    { 'fname' : 'KB'     , 'lname' : 'Tonel'   }
]

# iterate thru students and print first, last name
def printStudentNames(dict):
    for i in range(0, len(dict)):
        name = ""
        for val in dict[i].itervalues():
            name += val + " "
        #end for
        print name
    #end i
#end def

# run the code
print "\n" * 25
printStudentNames(students)
print "\n\nexiting..."
