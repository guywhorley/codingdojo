class Project

    attr_accessor :name, :description

    def initialize(name="Name", desc="Description")
        @name = name
        @description = desc
        self
    end

    def elevator_pitch
        return (@name + " " + @description)
    end

end
