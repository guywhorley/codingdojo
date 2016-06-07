# Example of Class Inheritance

class Animal

    def initialize
        puts "I'm alive!"
    end #def

    def breathe
        puts "Inhale and exhale"
    end
end #class

class Cat < Animal

    def jerk
        puts "scratching you"
    end #def

    def speak
        puts "Meow"
    end #def

end #Class

# TEST

Bella = Cat.new
Bella.breathe
Bella.jerk
Bella.speak
