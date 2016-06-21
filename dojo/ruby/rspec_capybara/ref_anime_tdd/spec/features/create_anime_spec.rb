require 'rails_helper'
require 'spec_helper'

# RUNNING WITHOUT SELENIUM --- IN HEADLESS MODE
#
# This test can run with just the 'do' and will still test
# the feature. A browser will not launch. If you comment in
# the :js => do block, then selenium will run the firefox browser, but
# execution time is slower.

RSpec.describe "create anime" do # , :js => true do
  scenario "creates new anime and redirects to anime page" do
    visit "/animes/new"

    fill_in 'name', with: 'Bob'
    click_button "submit"

    expect(current_url).to have_content('/animes')
    expect(page).to have_text("Bob")
  end
end
