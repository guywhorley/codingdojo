# name: human.rb
# auth: Guy Whorley
# desc: Model a human player

class Human

    attr_reader :name, :strength, :intelligence, :stealth, :health, :isAlive
    attr_writer :health

    # Public: create a human.
    # strength - physical prowess [integer]
    # intelligence - mental capacity [integer]
    # stealth - sneaking ability [integer]
    # health - life force [integer]
    def initialize(name="human")
        @playerType = "human"
        @name = name
        @strength = 3
        @intelligence = 3
        @stealth = 3
        @health = 100
        @isAlive = true
        self
    end

    # Public: display user statblock.
    def showStats
        stats = {
            :name => @name,
            :type => @playerType,
            :str  => @strength,
            :int  => @intelligence,
            :stlth => @stealth,
            :hp  => @health,
            :alive => @isAlive
        }
        puts stats.to_s
        self
    end

    # Public: provoke an attack upon another human.
    # enemy - the target of an attack
    # damage - maximum amount of damage
    def attack(enemy, damage=10)
        if @health < 0
            puts "#{@name} can't attack while UNCONSCIOUS OR DEAD!"
            return self
        end
        enemy.class.ancestors.any? do |w|
            if (w.to_s == "Human")
                if enemy.isAlive == true
                    puts "*** #{@name} is attacking #{enemy.name}! ***"
                    enemy.defend(rand(damage))
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

            if !@isAlive
                puts "#{@name} has moved on to the afterlife. Game over."
                exit
            end
            self
        end
end #class

class Wizard < Human

    def initialize(name="wizard")
        super(name)
        @playerType = "wizard"
        @health = 50
        @intelligence = 25
        puts "Creating wizard: #{@name}"
        self
    end

    # Public: Magical healing by 10 hps.
    def heal
        @health += 10
        puts "#{@name} the #{@playerType} heals self for 10 points."
        self
    end

    # Public: Magical fireball attack
    def fireball(enemy)
        puts "casting Fireball: 'Ars Magicus Igneous...'" if @health >= 0
        self.attack(enemy, 20)
        self
    end


end #class

class Ninja < Human

    def initialize(name="ninja")
        super(name)
        @playerType = "ninja"
        @stealth = 175
        puts "Creating ninja: #{@name}"
    end

    # Public: steal and heal
    def steal(enemy)
        puts "\n\nStealing: 'Gimme that...'" if @health >= 0
        self.attack(enemy)
        @health += 10
        puts "Ninja #{@name} gained 10 health!\n\n"
        self
    end

    def getAway
        puts "Ninja #{@name} uses wind-gets-away to escape"
        @health -= 15
        self
    end

end #class

class Samurai < Human

    @@samuraiCount = 0

    def initialize(name="samurai")
        super(name)
        @playerType = "samurai"
        @health = 200
        @@samuraiCount += 1
        puts "Creating samurai: #{@name}"
    end

    def deathBlow(enemy)
        puts "Samurai #{@name} invokes death blow, reducing #{enemy.name} to 0 health!"
        enemy.health = 0
        self
    end

    def meditate
        puts "Samurai #{@name} meditates, gaining full health"
        @health = 200
        self
    end

    def howMany
        puts "Number of samurai brotherhood: #{@@samuraiCount}"
        self
    end

end #class


#########
# FIGHT
#########
hillary = Samurai.new("Hillary")
hillary.showStats
trump = Ninja.new("Trump")
trump.showStats
hillary.howMany


trump.getAway.showStats
hillary.deathBlow(trump)
trump.steal(hillary)
hillary.meditate


while (hillary.isAlive && trump.isAlive)
    trump.attack(hillary)
    hillary.attack(trump)
end
