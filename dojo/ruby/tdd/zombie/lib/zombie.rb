class Zombie

    attr_accessor :name, :brains
    attr_reader :flesh_color

    def initialize(name="Ash")
        @name = name
        @brains = 0
        @flesh_color = ['blue', 'black', 'red', 'green']
    end

end
