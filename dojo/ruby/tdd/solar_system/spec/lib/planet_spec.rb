require 'spec_helper'
require 'solarsystem'

describe Planet do

    #   L E T  /  S U B J E C T

    subject { Planet.new("Earth", "Third rock from the sun",6000000000) }
    # let(:custom) { TestObject.new("myTest", 99) }

    #   M Y   T E S T S

    describe 'attributes' do
        it 'allows reading of :name' do
            expect(subject.name).to eq("Earth")
        end
        it 'allows reading of :description' do
            expect(subject.description).to eq("Third rock from the sun")
        end
        it 'allows reading of :population' do
            expect(subject.population).to eq(6000000000)
        end
    end
end
