# name: dragon.rb
# auth: Guy Whorley
# desc: Dragon class

require_relative 'Mammal'

class Dragon < Mammal

    def initialize
        @health = 170
        self
    end #def

    def fly
        puts "Flying... lose 10 health."
        @health -= 10
        self
    end #def

    def attackTown
        puts "Attacking town... lose 50 health"
        @health -= 50
        self
    end #def

    def eatHumans
        puts "Eating humans... gaining 20 health"
        @health += 10
        self
    end #def

end #class

# TEST

toothless = Dragon.new
toothless.attackTown.attackTown.attackTown.eatHumans.eatHumans.fly.fly.displayHealth
