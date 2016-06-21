require 'rails_helper'
require 'spec_helper'
require 'faker'

describe "Facebook login", :js => true do

    let (:login_url) { "https://www.facebook.com" }
    let (:submit) do
        sleep 5
        click_button("Log In")
        sleep 5
    end

    it "has login fields" do
        visit(login_url)
        expect(page).to have_field('email')
        expect(page).to have_field('pass')
        expect(find_button('Log In').value).to eq("Log In")
    end

    it "prevents login with empty email address" do
        visit(login_url)
        fill_in "pass", with: Faker::Internet.password(16)
        submit
        expect(current_path).to eq("/login.php")
    end

    it "prevents login with empty password" do
        visit(login_url)
        fill_in "email", with: Faker::Internet.email
        submit
        expect(current_path).to eq("/login.php")
    end

    it "gives proper error message when invalid email address is used" do
        visit(login_url)
        fill_in "email", with: "Somebody@somewhere"
        submit

        # CAPYBARA --- VIEW HIDDEN ELEMENTS --- *** TESTING TECHNIQUE
        # ENABLE ALL HIDDEN TEXT --- DO THE CHECK --- THEN TURN HIDE BACK ON
        Capybara.ignore_hidden_elements = false
        expect(page).to have_text("match any account.")
        Capybara.ignore_hidden_elements = true
        
        expect(current_path).to eq("/login.php")

    end

end
