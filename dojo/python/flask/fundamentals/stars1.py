# Star1.py
# Guy Whorley
# Create a function that takes a list of numbers and prints out '*' based on
#   an input array.
# 05/02/2016 - gcw - created

def draw_stars(arr):
    for i in range(0,len(arr)):
        line = ""
        for j in range(0,arr[i]):
            line += "*"
        #end inner for
        print line
    #end outer
#end def

# run the function
print "\n"*25
test = [2,3,6,10,5,2]
draw_stars(test)
print "\nExiting..."
