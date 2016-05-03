# Average List Assignment
# Author: Guy Whorley
# Print the average of te values in a list.
# 05/02/2016 - gcw - created file

a = [1, 2, 5, 10, 255, 3]
oracle = 46
sum = 0

# calculate sum of all vals in arr
for i in range(0,len(a)):
    sum += a[i]

# get average
avg = sum/len(a)

# check against test oracle
assert avg == 46, "Expected avg of 46 was not found."

# display average
print "Average of array is:", avg
