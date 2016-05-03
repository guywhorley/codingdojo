# Multiply
# Guy Whorley
# Create a function called 'multiply' that reads each value in the lsit and
#   returns a list where each value has been mulitiplied by 5.
# 05/02/2015 - gcw - created file


# multiply an array
def multiply(arr):
    results = []
    if len(arr) == 0:
        pass
    else:
        for i in range(0, len(arr)):
            results.append(arr[i]*arr[i])
    return results
#end def

# test-it
arr = [1,2,3,4,5]
results = multiply(arr)
assert (arr[0]*arr[0]) == results[0], "Expected value not found."

print "Orig: {}".format(arr)
print "Post: {}".format(results)
