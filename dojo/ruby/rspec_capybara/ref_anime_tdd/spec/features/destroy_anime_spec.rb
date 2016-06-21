require 'rails_helper'

RSpec.describe "deleteing anime" do

  it "destroys the anime" do

    Anime.create(name: 'Bella')
    visit '/animes'
    expect(page).to have_text('Bella')

    click_button "delete"
    expect(page).not_to have_text("Bella")
    
  end


end
