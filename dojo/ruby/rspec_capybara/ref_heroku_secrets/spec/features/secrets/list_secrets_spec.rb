require 'rails_helper'

RSpec.describe 'user profile page' do

  before do
    @user = create_user
    puts @user.inspect
    log_in @user
  end

  it "displays a user's secrets" do
    # create a test secret
    secret = @user.secrets.create(content: 'secret world')
      # puts "Secret content: #{secret.content}"
    # go to profile page
    visit "/users/#{@user.id}"
    expect(page).to have_text(secret.content)
  end

  it "displays everyone's secrets" do
    secret1 = Secret.create(content: 'secret', user_id: @user.id)

    user2 = create_user 'moka', 'moka@dog.com'
    secret2 = user2.secrets.create(content: 'secret')

    visit '/secrets'
    expect(page).to have_text(secret1.content)
    expect(page).to have_text(secret2.content)
  end

end
