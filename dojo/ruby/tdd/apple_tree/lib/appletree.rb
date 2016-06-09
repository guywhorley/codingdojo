class AppleTree

    attr_reader :height, :age, :appleCount

    def initialize
        @height = 0
        @age = 0
        @appleCount = 0
        self
    end

    def yearGoneBy
        @age += 1
        @height += 10 if @age < 11
        @appleCount = (@age * 100) if (@age > 3 and @age < 11)
        @appleCount = 0 if @age >= 11
        self
    end

    def pickApples
        @appleCount = 0
        self
    end

end
