require 'rails_helper'

RSpec.describe UsersController, type: :controller do

  before do
    @user = create_user
  end

  describe "when signed in as the wrong user" do
    before do
      @wrong_user = create_user 'cicero', 'roman@poet.com'
      session[:user_id]= @wrong_user.id
    end
    it "cannot access profile page of another user" do
      # Example: How to call class methods and pass param
      get :edit, id: @user
      expect(response).to redirect_to("/users/#{@wrong_user.id}")
    end
    it "cannot update another user" do
      patch :update, id: @user
      expect(response).to redirect_to("/users/#{@wrong_user.id}")
    end
    it "cannot destroy another user" do
      delete :destroy, id: @user
      expect(response).to redirect_to("/users/#{@wrong_user.id}")
    end
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
