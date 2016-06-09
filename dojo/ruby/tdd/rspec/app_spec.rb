require 'spec_helper'
# require '<CLASS-UNDER-TEST>'

# example of a class that is being tested, this would normally
# reside in it's own ruby file.
class TestObject
       attr_accessor :name, :count
       def initialize(name="Bob", count=42)
           @name = name
           @count = count
       end #init
end #class

describe '<CLASS_UNDER_TEST>' do

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

    describe 'attributes' do  # test getters, setters
        it 'has default values' do
            expect(subject.name).to eq('Bob')
            expect(subject.count).to eq(42)
        end
        it 'has custom values' do
            expect(custom.name).to eq('myTest')
            expect(custom.count).to eq(99)
        end
    end

    describe '.my_class_method' do  # test class methods
        # TODO
    end

    describe '#my_instance_method' do  # test instance methods
        # TODO
    end
end
