require 'spec_helper'
require 'solarsystem'

describe 'SolarSystem' do

    #   L E T   /  S U B J E C T
    subject { TestObject.new }  # subject shortcut
    let(:custom) { TestObject.new("myTest", 99) }

    #   M Y   T E S T S

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

    # describe '.my_class_method' do  # test class methods
    #     # TODO
    # end

    describe '#my_instance_method' do  # test instance methods
        # TODO
    end
end
