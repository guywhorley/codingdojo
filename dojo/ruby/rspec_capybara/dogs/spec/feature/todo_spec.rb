require 'rails_helper'



describe "Family" do

    let(:person) { Person.new("Bob", 99) }
    let(:pet) { Pet.new()}


    xit "is a valid person's name" do
        expect(person.name).to be_valid
    end

    xit "is a valid pet's name" do
        expect(pet.name).to be_valid
    end

    xit "is a valid age for a person" do
        expect(person.age).to be_valid
    end

    xit "is a valid age for a pet" do
        expect(pet.age).to be_valid
    end

end
