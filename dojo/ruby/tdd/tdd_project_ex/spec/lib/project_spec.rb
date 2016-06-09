require 'spec_helper'
require 'project'

describe Project do

    #  L E T  /  S U B J E C T
    subject { Project.new }

    #  M Y   T E S T S
    describe 'attributes' do
        it 'allows read/write for :name' do
            subject.name = "Project1"
            expect(subject.name).to eq('Project1')
        end
        it 'allows read/write for :description' do
            subject.description = "foo"
            expect(subject.description).to eq("foo")
        end
    end

    # describe '.my_class_method' do  # test class methods
    #     # TODO
    # end

    describe '# instance methods' do  # test instance methods
        it 'has elevator_pitch to explain name and description' do
            expect(subject.elevator_pitch).to eq("Name Description")
        end
    end
end
