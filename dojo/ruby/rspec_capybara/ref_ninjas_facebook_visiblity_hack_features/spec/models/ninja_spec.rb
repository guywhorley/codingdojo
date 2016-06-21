require 'rails_helper'

RSpec.describe "Ninja Model", type: :model do

    it "should not save if ninja_name is too short" do
        ninja = Ninja.new(ninja_name: 'n')
        expect(ninja).to be_invalid
    end
    it "should not save if ninja_name is missing" do
        ninja = Ninja.new(ninja_name: '')
        expect(ninja).to be_invalid
    end
    it "should not save if ninja_description is too short" do
     ninja = Ninja.new(ninja_description: 'd')
     expect(ninja).to be_invalid
    end
    it "should not save if ninja_description is missing" do
     ninja = Ninja.new(ninja_description: '')
     expect(ninja).to be_invalid
    end
    it "should save with valid name, description lengths" do
        ninja = Ninja.new(ninja_name: 'Bob', ninja_description: 'Ninja guy')
        expect(ninja).not_to be_invalid
    end

end
