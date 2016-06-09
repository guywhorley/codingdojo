require 'spec_helper'
require 'human'


describe Wizard do

    ################
    #  LET/DOUBLES
    ################
    subject { Wizard.new("Malfoy") }
    let(:enemy) { Ninja.new }

    ###################
    # MY TESTS HERE...
    ###################

    describe "wizard" do
        it "has human in ancestor chain" do
            expect(subject.class.ancestors).to include(Human)
        end
        it 'has fireball attack that reduces enemy health' do
            subject.fireball(enemy)
            expect(enemy.health).to be_between(80, 99).inclusive
        end
    end

    describe 'attributes' do  # test getters, setters
        it 'has default health and intelligence' do
            expect(subject.health).to eq(50)
            expect(subject.intelligence).to eq(25)
        end
    end

    describe '#heal' do
        it "heals wizard by 10 points" do
            subject.heal
            expect(subject.health).to eq(60)
        end
    end
end
