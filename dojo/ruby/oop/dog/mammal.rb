# Example of Class Inheritance

class Mammal

    attr_accessor :alive

    def initialize
        @health = 150
        @alive = true
        self
    end #def

    def breathe
        puts "Inhale and exhale"
        self
    end

    def displayHealth
        puts "Health: #{@health}"
        self
    end

end #class
