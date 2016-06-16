require 'rails_helper'

describe UsersController do
    
  it "routes /users/index to the users controller" do
    expect(:get => "/users/index").to route_to(:controller => "users", :action => "index")
  end

  it "routes /users/:id to users profile" do
    expect(:get => "/users/1").to route_to(:controller => "users", :action => "show", :id => "1")
  end

end

# RSpec.describe UsersController, type: :controller do
  # describe "GET #index" do
  #   it "returns http success" do
  #     get :index
  #     expect(response).to have_http_status(:success)
  #   end
  # end
  #
  # describe "GET #create" do
  #   it "returns http success" do
  #     get :create
  #     expect(response).to have_http_status(:success)
  #   end
  # end
  #
  # describe "GET #new" do
  #   it "returns http success" do
  #     get :new
  #     expect(response).to have_http_status(:success)
  #   end
  # end
# end
