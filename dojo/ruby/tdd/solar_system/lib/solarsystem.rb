class Planet

    attr_reader :name, :description, :population

    def initialize(name="name", description="desc", population=0)
        @name = name
        @description = description
        @population = population
        self
    end

    def to_s
        return @Name
    end
end

class SolarSystem

    attr_reader :name, :planets, :planetCount

    def initialize(name="Milky Way")
        @name = name
        @planets = []
        @planetCount = 0
        self
    end

    def addPlanet(planet)
        @planets << planet.name if planet.instance_of?(Planet)
        @planetCount +=1 if planet.instance_of?(Planet)
    end

    def superNova
        @planets = []
        @planetCount = 0
    end

end
