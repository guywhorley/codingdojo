# name: dog.rb
# auth: Guy Whorley
# desc: Dog class

require_relative 'Mammal'

class Dog < Mammal

    def pet
        @health += 5
        puts "Petting dog... gaining 5 health."
        self
    end #def

    def walk
        puts "Walking dog... losing 1 health"
        @health -= 1
        self
    end

    def run
        puts "Running dog... losing 10 health"
        @health -= 10
        self
    end

end #class

# TEST

Moka = Dog.new
Moka.displayHealth
Moka.walk.walk.walk.run.run.pet.displayHealth
