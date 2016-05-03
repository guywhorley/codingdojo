#
# Sum List Assignment
# Author: Guy Whorley
# Create a program that prints the sum of all the values in a given list.
# 05/02/2016 - gcw - created file

# source arr
a = [1, 2, 5, 10, 255, 3]

sum = 0;
for i in range(0, len(a)):
    sum += a[i]

assert sum == 276, "sum should be 176, but is not."
print "Sum of Array is:",str(sum)
