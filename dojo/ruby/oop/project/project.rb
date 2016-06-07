# name: project.rb
# author: Guy Whorley
# description: generic project class

class Project

    attr_accessor :project_description, :project_name

    def initialize(name, description)
        @project_name = name
        @project_description = description
        self
    end #def

    def elevatorPitch
        puts "Project Name: #{@project_name}"
        puts "Description: #{@project_description}"
        self
    end #def

end #class

proj = Project.new('Runway', 'Create a third runway')
# puts "Project-name: #{proj.project_name}"
proj.elevatorPitch
