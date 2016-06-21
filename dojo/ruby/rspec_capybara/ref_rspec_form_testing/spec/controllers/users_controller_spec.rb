require 'rails_helper'

describe UsersController, type: :controller do

    context 'when routing'
    it "#new" do
        expect(:get => "/users/new").to route_to(:controller => "users", :action => "new")
    end
    
    it "returns returns success" do
      get :new
      expect(response).to have_http_status(:success)
    end

end
