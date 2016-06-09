# name: project.rb
# author: Guy Whorley
# description: generic project class

class Project

    attr_accessor :project_description, :project_name
    attr_reader :teamMembers
    
    def initialize(name, description)
        @project_name = name
        @project_description = description
        @teamMembers = []
        self
    end

    def elevatorPitch
        puts "Project Name: #{@project_name}"
        puts "Description: #{@project_description}"
        self
    end

    def addToTeam(name)
        @teamMembers << name
    end

end #class
