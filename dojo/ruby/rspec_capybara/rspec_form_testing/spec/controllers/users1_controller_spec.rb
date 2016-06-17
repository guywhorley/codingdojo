require 'rails_helper'

RSpec.describe UsersController, type: :controller do

    it "routes to #new" do
        expect(:get => "/users/new").to route_to(:controller => "users", :action => "new")
    end

    it "returns http success" do
      get :new
      expect(response).to have_http_status(:success)
    end

end
