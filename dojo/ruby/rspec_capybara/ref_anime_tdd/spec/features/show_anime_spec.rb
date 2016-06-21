require 'rails_helper'
require 'faker'

RSpec.describe "anime show page" do

  it "displays information about an anime" do

    # CREATE THE TEST DATA NEEDED FOR TEST
    anime = Anime.create(name: Faker::Internet.user_name )

    visit "/animes/#{anime.id}"
    expect(page).to have_text(anime.name)
  end

end
