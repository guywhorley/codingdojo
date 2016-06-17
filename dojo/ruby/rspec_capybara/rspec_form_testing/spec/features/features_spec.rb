require 'rails_helper'
require 'faker'

RSpec.describe "Registration", :js => true do

    scenario "has expected form fields " do
        visit "http://localhost:3000/users/new"
        expect(page).to have_field('first_name')
        expect(page).to have_field('last_name')
        expect(page).to have_field('email')
        expect(page).to have_field('password')
        expect(page).to have_field('password_confirmation')
    end

    scenario "successfully register a new user" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).to have_content "Success"
    end

    scenario "user cannot register with empty first name" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        # fill_in "first_name", with:  Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "user cannot register with empty last name" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        # fill_in "last_name", with: fn
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "user cannot register with invalid email" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: "somerandomthing"
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "user cannot register with empty password" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        # fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "user cannot register with password < 6 characters" do
        pwd = Faker::Internet.password(4)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "user cannot register with empty confirmation password" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        # fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "user cannot register with missmatched passwords" do
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: Faker::Internet.password(6)
        fill_in "password_confirmation", with: Faker::Internet.password(6)
        click_button "Register"
        expect(page).not_to have_content "Success"
    end

    scenario "successfully register after a failed attempt" do
        pwd = Faker::Internet.password(6)
        visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        # fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).not_to have_content "Success"

        page.driver.go_back

        # visit "http://localhost:3000/users/new"
        fill_in "first_name", with: Faker::Internet.user_name
        fill_in "last_name", with: Faker::Internet.user_name
        fill_in "email", with: Faker::Internet.email
        fill_in "password", with: pwd
        fill_in "password_confirmation", with: pwd
        click_button "Register"
        expect(page).to have_content "Success"
    end

end
