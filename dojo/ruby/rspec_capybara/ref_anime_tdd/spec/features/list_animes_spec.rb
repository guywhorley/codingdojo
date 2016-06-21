require 'rails_helper'

RSpec.describe 'Listing of Animes' do

    it "displays list of existing animes" do
        ani1 = Anime.create(name: 'Moka')
        ani2 = Anime.create(name: 'Maggie')
        ani3 = Anime.create(name: 'Bella')

        visit ('/animes')

        expect(page).to have_text(ani1.name)
        expect(page).to have_text(ani2.name)
        expect(page).to have_text(ani3.name)
    end
end
