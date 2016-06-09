require 'spec_helper'
require 'project'

describe Project do

    ################
    #  LET/DOUBLES
    ################
    subject { TestObject.new }  # subject shortcut
    let(:custom) { TestObject.new("myTest", 99) }

    ##############################
    # METHOD HOOKS .before/.after
    ##############################

    # before(:context) do  # RUN 1X BEFORE CONTEXT
    # end

    # before(:all) do  # RUN 1X BEFORE ALL SPECS BUT AFTER CONTEXT
    # end

    # after(:context) do  # RUN 1X AFTER ALL SPECS ARE RUN
    # end

    # before(:each) do  # RUN BEFORE EACH SPEC
    # end

    #after :example do  # RUN ATER EACH SPEC
    #end

    # around(:example) do |example|  #  Run this around EACH spec
        # puts "... in around.example"
        # puts "... [code to run before example]"
        # example.run
        # puts "... [code to run after example]"
    # end

    ###################
    # MY TESTS HERE...
    ###################
    let(:proj1) { Project.new("Proj1", "desc1") }
    let(:proj2) {
        p2 = Project.new("Proj2", "desc2")
        p2 .addToTeam("Fran")
        return p2
    }

    # Setters / Getters
    describe '.attributes' do
        it 'allows read/write on :project_description' do
            proj1.project_description = "mod_desc1"
            expect(proj1.project_description).to eq("mod_desc1")
        end
        it 'allows read/write on :project_name' do
            proj1.project_name = "mod_proj1"
            expect(proj1.project_name).to eq("mod_proj1")
        end
        it 'allows read on :teamMembers' do
            expect(proj2.teamMembers).to include('Fran')
        end
    end

    describe '.Class-Methods-All' do  # test class methods
    end

    describe '#Instance-methods-All' do  # test instance methods
        it "gives the elevatorPitch" do
            expect { proj2.elevatorPitch }.to output(/Project Name: Proj2/).to_stdout
            expect { proj2.elevatorPitch }.to output(/Description: desc2/).to_stdout
        end
        it "allows addToTeam" do
            proj1.addToTeam("Bob")
            expect(proj1.teamMembers).to include("Bob")
        end
    end





end
