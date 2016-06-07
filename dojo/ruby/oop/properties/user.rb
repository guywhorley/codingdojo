# User
# This class represents users.


class User # lowercase 'class', Capitalize <Name>
    attr_accessor :first_name, :last_name  # shortcut getter/Setter

    def initialize(first_name, last_name)
        @first_name = first_name
        @last_name = last_name
    end

    # OLD SKOOL GETTER, SETTER
    # Setter
    # def first_name(val)
    #     @first_name = val
    # end

    # Getter
    # def first_name
    #     @first_name # Ruby returns whatever was eval last
    # end
end
