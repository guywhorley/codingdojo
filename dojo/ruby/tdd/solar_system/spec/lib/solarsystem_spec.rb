require 'spec_helper'
require 'solarsystem'


describe SolarSystem do

    #   L E T  /  S U B J E C T

    subject do
        ss = SolarSystem.new()
        mercury = Planet.new("Mercury","First",0)
        venus = Planet.new("Venus","Second",0)
        ss.addPlanet(mercury)
        ss.addPlanet(venus)
        return ss
    end
    let(:planets) { ['Mercury','Venus'] }

    #   M Y   T E S T S

    describe '++ attributes' do
        it 'allows reading of :name' do
            expect(subject.name).to eq('Milky Way')
        end
        it 'sets default name to Milky Way' do
            expect(subject.name).to eq('Milky Way')
        end
        it 'contains added planets' do
            expect(subject.planetCount).to eq(2)
            expect(subject.planets).to include("Mercury", "Venus")
        end
        it 'allows reading of :planetCount' do
            expect(subject.planetCount).to eq(2)
        end
    end

    describe '# instance methods' do  # test instance methods
        it 'superNova destroys all planets in solar system' do
            subject.superNova
            expect(subject.planetCount).to eq(0)
            expect(subject.planets.length).to eq(0)
        end
        it 'allows adding of planets to solar system.' do
            expect(subject.planets).to contain_exactly('Mercury', 'Venus')
        end

    end
end
