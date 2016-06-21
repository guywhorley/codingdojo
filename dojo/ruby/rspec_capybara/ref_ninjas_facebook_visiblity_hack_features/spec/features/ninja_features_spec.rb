require 'rails_helper'
require 'spec_helper'

RSpec.describe "Features", :js => true do

    describe "Register" do

      it "has name and description fields" do
        visit "http://localhost:3000"
        # sleep 10
        expect(page).to have_field('ninja_name')
        expect(page).to have_field('ninja_description')
        expect(find_button('Submit').value).to eq("Submit")
      end

      it "creates ninja and redirects to success page" do
        visit "/"
        fill_in "ninja_name", with: "Danielsan"
        fill_in "ninja_description", with: "wax on wax off"
        click_button "Submit"
        expect(current_path).to eq("/success")
        expect(page).to have_text("Form submitted succesfully!")
      end

      it "displays error message when name is missing" do
          visit "http://localhost:3000"
          expect(page).to have_field('ninja_name')
          fill_in "ninja_description", with: "wax on wax off"
          expect(find_button('Submit').value).to eq("Submit")
          click_button "Submit"
          expect(page).to have_text("Ninja name can't be blank")
          expect(page).to have_text("Ninja name is too short")
      end

      it "displays error message when name is too short" do
          visit "http://localhost:3000"
          expect(page).to have_field('ninja_name')
          fill_in "ninja_name", with: "n"
          fill_in "ninja_description", with: "wax on wax off"
          expect(find_button('Submit').value).to eq("Submit")
          click_button "Submit"
          expect(page).not_to have_text("Ninja name can't be blank")
          expect(page).to have_text("Ninja name is too short")
      end

      it "displays error message when description is missing" do
          visit "http://localhost:3000"
          expect(page).to have_field('ninja_description')
          fill_in "ninja_name", with: "danielsan"
          expect(find_button('Submit').value).to eq("Submit")
          click_button "Submit"
          expect(page).to have_text("Ninja description can't be blank")
          expect(page).to have_text("Ninja description is too short")
      end

      it "displays error message when description is too short" do
          visit "http://localhost:3000"
          expect(page).to have_field('ninja_description')
          fill_in "ninja_name", with: "danielsan"
          fill_in "ninja_description", with: "w"
          expect(find_button('Submit').value).to eq("Submit")
          click_button "Submit"
          expect(page).not_to have_text("Ninja name can't be blank")
          expect(page).to have_text("Ninja description is too short")
      end
    end
end
