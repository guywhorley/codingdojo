require 'spec_helper'
require 'zombie'

# TOP-LEVEL EXAMPLE GROUP
describe Zombie do
    # NESTED-GROUPS

    #INITIALIZE
    context 'when zombie uses default values' do
        it "has the default name" do
            z = Zombie.new
            #puts ('Getting default name...')
            expect(z.name).to eq('Ash') # to match('Ash')
            #expect(z.name).not_to match('Ash') # can omit not_to parens
        end

        it "has the default amount of brains" do
            z = Zombie.new
            expect(z.brains).to eq(0)
        end

        it "has default flesh color" do
            skip("Need to work out colors... issue#{145001}")
            z = Zombie.new
            colors = ['blue', 'black', 'red', 'green']
            expect(z.flesh_color).to match_array(colors)
        end
    end

    context 'when zombie has custom values' do
        it "has custom name" do
            z = Zombie.new("Bob")
            expect(z.name).to eq('Bob')
        end
    end

    #ATTRIBUTES
    describe 'attributes' do
        pending("Still need to implement")
        it "allows reading and writing for :name" do

        end

        it "allows reading and writing for :brains" do

        end

        it "allows reading for :flesh_color" do

        end



    end

    #CLASS METHODS
    describe '.my_class_method' do #convention is prepend name w/ "."
        # TODO
    end

    #INSTANCE METHODS
    describe '#my_instance_method' do
        # TODO
    end

end #zombie spec
