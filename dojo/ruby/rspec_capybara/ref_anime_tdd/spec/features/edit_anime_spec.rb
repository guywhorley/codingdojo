require 'rails_helper'
require 'byebug'

RSpec.describe "edit anime" do # , :js => true do

  it "displays an edit form with anime values pre-populated" do

    anime = Anime.create(name: Faker::Internet.user_name)
    visit "/animes/#{anime.id}/edit"

    # byebug

    # expect(page).to have_text "#{anime.name}"
    expect(page).to have_text "Edit Anime"
    expect(find_field('name').value).to eq(anime.name)

  end

end
