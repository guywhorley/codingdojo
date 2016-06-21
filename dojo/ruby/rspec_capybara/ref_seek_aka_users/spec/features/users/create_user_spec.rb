require 'rails_helper'

RSpec.describe 'creating a user' do

  before do
    visit '/users/new'
  end

  it 'creates a new user and redirects to profile page with proper credentials' do
      fill_in 'email', with: 'roger@rabbit.wb'
      fill_in 'name', with: 'Roger'
      fill_in 'password', with: 'password'
      fill_in 'password_confirmation', with: 'password'
      click_button 'Join'
      last_user = User.last
      expect(current_path).to eq("/users/#{last_user.id}")
  end

  it 'shows validation errors without proper validation' do
    click_button "Join"
    expect(current_path).to eq('/users/new')
    expect(page).to have_text("Change values")
  end

end
