class UsersController < ApplicationController

  def index
    # # :id is passed from session controller in URL, lookup user
    # # and pass into view
    @user = User.find_by(id: params[:id])
  end

  def show
    # :id is passed from session controller in URL, lookup user
    # and pass into view
    @user = User.find_by(id: params[:id])
  end

end
