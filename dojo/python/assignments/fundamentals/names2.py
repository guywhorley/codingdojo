# Names Part II
# Guy Whorley
# Create a program that manipulates dictionaries
# 05/02/2016 - gcw - created

users = {
'Students': [
    { 'fname' : 'Michael', 'lname' : 'Jordan'  },
    { 'fname' : 'John'   , 'lname' : 'Rosales' },
    { 'fname' : 'Mark'   , 'lname' : 'Guillen' },
    { 'fname' : 'KB'     , 'lname' : 'Tonel'   }
],
'Instructors': [
    { 'fname' : 'Michael', 'lname' : 'Choi'  },
    { 'fname' : 'Martin'   , 'lname' : 'Puryear' }
]
}
# iterate thru students and print first, last name
def printStudentsAndTeachersNames(dict):
    # get keys // Students; Instructors
    # for each key, get val: iter thru each val array
    for k, data in dict.items():
        print k
        for i in range(0,len(data)):
            name = ""
            for val in data[i].itervalues():
                name += val + " "
            #end i
            print str(i) + " - " + name.upper() + "- " + str(len(name))
    #end k,data
#end def

# run the code
print "\n" * 25
printStudentsAndTeachersNames(users)
print "\n\nexiting..."
