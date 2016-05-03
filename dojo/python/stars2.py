# Stars2.py
# Guy Whorley
# Create a function that takes a list of numbers and prints out the first letter
#   of the string that is passed in (lower case only).
# 05/02/2016 - gcw - created

def draw_stars(arr):

    for i in range(0,len(arr)):
        line = "" # reset line for current pass
        sourceLine = arr[i]
        maxOuter = 0;
        glyph = "*" #default symbol for number lines
        if type(sourceLine) is int: # he's a number, JIM
            maxOuter = sourceLine
        else:  # string instead
            maxOuter = len(sourceLine)
            glyph = sourceLine[0].lower() # get alpha glyph to use for line
        for j in range(0, maxOuter):
            line += glyph
        #end inner for
        print line
    #end outer
#end def

# run the function
print "\n"*25
test = [2,"Chris",3,"Moka",6, "hello",10,5,2]
draw_stars(test)
print "\nExiting..."
