# filename: my_enumerable.rb
# author: Guy Whorley
# description: custom module based on Enumerable

module MYENUMERABLE
    def my_each
        # iterate thru the array
        i = 0
        while i < self.length
            # pass the current array value to the block
            yield self[i]
            i += 1
        end #while
        return self
    end #def
end #end module

# Include my custom enumerable in the standard Ruby classes
# listed below

class Array
    include MYENUMERABLE
end #class

# [1,2,3].each { |i| i*2 }
[1,2,3,4].my_each { |i| print i, " " } #prints 1 2 3 4 in the terminal
