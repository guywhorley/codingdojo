# This class represents the Coding Dojo

class CodingDojo

    @@no_of_branches = 0

    # PUBLIC METHODS (Default level)
    def initialize(id, name, address)
        @branch_id = id
        @branch_name = name
        @branch_address = address
        @@no_of_branches += 1
        puts "\nCreated branch #{@@no_of_branches}"
    end #def

    def to_s
        return "[id:#{@branch_id}, name:#{@branch_name}, addr:#{@branch_address}]"
    end #def

    # PROTECTED METHODS
    protected
    def myProtectedMethod1()
    end

    private
    def myPrivateMethod1()
    end




end #class

########
# TEST
########

branch = CodingDojo.new(1, "Seattle CodingDojo", "Bellevue, Wa")
branch2 = CodingDojo.new(2, "Everett CodingDojo", "Everett, Wa")

puts branch.to_s
puts branch2.to_s
