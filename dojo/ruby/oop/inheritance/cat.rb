# CAT
require_relative 'Animal'

class Cat < Animal

    def jerk
        puts "scratching you"
        self
    end #def

    def speak
        puts "Meow"
        self
    end #def

    def whoAmI
        puts self
        self
    end

end #Class

# TEST

Bella = Cat.new
Bella.breathe.jerk.speak.whoAmI
