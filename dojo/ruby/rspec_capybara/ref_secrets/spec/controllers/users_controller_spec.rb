require 'rails_helper'

RSpec.describe UsersController, type: :controller do

  before do
    @user = create_user
  end

  describe "when not logged in" do
    before do
      session[:user_id] = nil
    end
    it "cannot access show" do
      # Example: How to call class methods and pass param
      get :show, id: @user
      expect(response).to redirect_to('/sessions/new')
    end
    it "cannot access edit" do
      get :edit, id: @user
      expect(response).to redirect_to('/sessions/new')
    end
    it "cannot access update" do
      get :update, id: @user
      expect(response).to redirect_to('/sessions/new')
    end
    it "cannot access destroy" do
      get :destroy, id: @user
      expect(response).to redirect_to('/sessions/new')
    end
  end

end
