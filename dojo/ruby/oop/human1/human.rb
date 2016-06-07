# name: human.rb
# auth: Guy Whorley
# desc: Model a human player

class Human

    attr_reader :name, :strength, :intelligence, :stealth, :health, :isAlive

    # Public: create a human.
    # strength - physical prowess [integer]
    # intelligence - mental capacity [integer]
    # stealth - sneaking ability [integer]
    # health - life force [integer]
    def initialize(name="player-human")
        @name = name
        @strength = 3
        @intelligence = 3
        @stealth = 3
        @health = 100
        @isAlive = true
        self
    end

    # Public: provoke an attack upon another human.
    # enemy - the target of an attack
    def attack(enemy)
        if @health < 0
            puts "#{@name} can't attack while UNCONSCIOUS OR DEAD!"
            return self
        end
        enemy.class.ancestors.any? do |w|
            if (w.to_s == "Human")
                if enemy.isAlive == true
                    puts "\n\n*** #{@name} is attacking #{enemy.name}! ***"
                    enemy.defend(rand(70))
                else
                    puts "#{enemy.name} is already DEAD! #{@name} is aborting attack."
                end
            end
        end
        self
    end

    # Public: defend from attack
    def defend(weaponDamage)
        isDead?(weaponDamage)
        self
    end

    private

        def isDead?(damage)
            @health -= damage
            puts "#{@name} has taken #{damage} points of damage! Health: #{@health}"
            puts "#{@name} is unconscous!" if (@health < 0 && @health > -10)
            puts "#{@name} is dead!" if @health <= -10
            @isAlive = false if @health <= -10
            self
        end
end #class

# FIGHT
hillary = Human.new("Hillary")
trump = Human.new("Trump")

trump.attack(hillary)
hillary.attack(trump)

trump.attack(hillary)
hillary.attack(trump)

trump.attack(hillary)
hillary.attack(trump)

trump.attack(hillary)
hillary.attack(trump)

trump.attack(hillary)
hillary.attack(trump)
