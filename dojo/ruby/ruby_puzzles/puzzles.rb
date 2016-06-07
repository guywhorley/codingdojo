# Ruby Puzzles
# Author: Guy Whorley

# return an array having elements greater or equal to min
def floor(arr, min)
    sum = 0
    arr.each do |num|
        sum += num
    end
    temp = arr.reject { |n| n < min }
    puts "Sum of array:#{sum}"
    return temp
end

# Shuffle array, print, and return only those elements where
# element length is greater or equal to len.
def shuffleKeepGreaterThanLength(arr, len)
    temp = arr.shuffle.to_s
    puts temp.to_s
    return arr.reject { |s| s.length < 6 }
end

# Alphabet Array Fun
# Create alphabet array, shuffle, display first and last element.
# Print message if first letter is a vowel.
def alphaFun()
    arr = ('a'...'z').to_a.shuffle
    puts arr.to_s
    puts "First letter of array: #{arr.first}"
    puts "Last letter of array: #{arr.last}"
    if ['a','e','i','o','u'].include? arr.first
        puts "First letter is a vowel"
    end
end 

# Generate array with random integers where numbers are between
# min and max inclusive.
def getRndIntArray(numElements, minValue, maxValue)
    arr = []
    rnd = Random.new
    diff = (maxValue - minValue)
    for i in 0..(numElements-1)
        arr.push(attrNum = rnd.rand(diff) + minValue)
    end
    return arr
end

# Util method for min element
def showMin(arr)
    puts "Arr min:#{arr.min}"
end

# Util method for showing max element
def showMax(arr)
    puts "Arr max:#{arr.max}"
end

# Build random Int array, sort, display arr, show min, show max
def randomArrayFun()
    arr = getRndIntArray(10, 55, 100)
    puts arr.sort!.to_s
    showMin(arr)
    showMax(arr)
end

# Build a random string that is 5 characters long
def buildRndString(len)
    str = ""
    for i in 0..4
        str += (65 + rand(26)).chr
    end
    return str
end

# Build an array with 10 random strings that are 5 chars long.
def buildRndStringArray(arrLength, strLength)
    arr = []
    for i in 0..arrLength-1
        arr.push(buildRndString(strLength))
    end
    return arr
end

#########
# TESTS
#########

# Generate array with 10 random strings, 5 chars long
puts buildRndStringArray(10,5).to_s

# build random string 5 chars long
#puts buildRndString(5)

# Build randInt array, sort, display arr, show min, show max
# randomArrayFun()

# puts getRndIntArray(10, 55, 100).sort!.to_s
# puts getRndIntArray(10, 55, 100).to_s


# puts getRndIntArray(10, 55, 100).to_s
# alphaFun()

# myNames = %w{John, KB, Oliver, Cory, Matthew, Christopher}
# myArr = [3,5,1,2,7,9,8,13,25,32]
# puts myArr.to_s
# puts floor(myArr,10).to_s

#puts myNames.to_s
#puts shuffleKeepGreaterThanLength(myNames, 5).to_s
