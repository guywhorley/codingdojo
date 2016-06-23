require 'rails_helper'

RSpec.describe 'update user' do

  it 'updates user and redirects to profile page' do
    user = create_user
    puts "(Creating User) Username: => '#{user.name}', password: => '#{user.email}'"
    log_in user
    expect(page).to have_text("brain")
    click_link "Edit Profile"
    fill_in "name", with: "Pinky"
    fill_in "email", with: "pinky@sidekick.edu"
    fill_in "password", with: '123'
    fill_in "password_confirmation", with: '123'
    click_button "Update"
    expect(page).not_to have_text("brain")
    expect(page).to have_text("Pinky")
  end

  # it 'DEBUG: updates user and redirects to profile page' do #, :js => true do
  #   user = User.create(
  #     name: 'chris',
  #     email: 'chris@whorley.com',
  #     password: '123',
  #     password_confirmation: '123'
  #   )
  #
  #   visit '/sessions/new'
  #
  #   fill_in 'Email', with: 'chris@whorley.com'
  #   fill_in 'Password', with: '123'
  #   click_button 'Submit'
  #   expect(current_path).to eq("/users/#{user.id}")
  #   expect(page).to have_text("chris")
  #
  #   expect(page).to have_link "Edit Profile"
  #   click_link "Edit Profile"
  #   fill_in "name", with: "brain"
  #   fill_in "email", with: "brain@worldconquest.com"
  #   fill_in "password", with: '123'
  #   fill_in "password_confirmation", with: '123'
  #   click_button "Update"
  #   expect(page).not_to have_text("chris")
  #   expect(page).to have_text("worldconquest")
  # end

end
