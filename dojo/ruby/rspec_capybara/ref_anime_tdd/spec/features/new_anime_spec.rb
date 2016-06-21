require 'rails_helper'

RSpec.describe "new anime page" do

  it "displays correct form fields to create new anime" do
    visit "/animes/new"
    expect(page).to have_field('name')
  end
end
