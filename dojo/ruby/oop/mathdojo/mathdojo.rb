# file: mathdojo.rb
# auth: Guy Whorley
# desc: Math class

class MathDojo

    attr_accessor :total

    def initialize
        @total = 0
        self
    end

    # add operands
    def add(x=0, y=0)
        @total += (x+y)
        self
    end

    # return the difference between the subtrahend and the minuend
    def subtract(x=0, y=0)
        @total -= (x + y)
        self
    end

    # show result
    def result
        return @total
        self
    end

    private

        def clearTotal
            @total = 0
            self
        end

end #class

# TEST

md = MathDojo.new

result = md.add(2).add(7,4).subtract(3,2).result
puts result
