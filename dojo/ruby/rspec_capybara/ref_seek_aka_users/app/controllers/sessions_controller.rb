class SessionsController < ApplicationController

  def new
  end

  def create
    # Initially, find the user by email. If exists, then check
    # for matching password via bcrypt
    @user = User.find_by email: params[:Email]

    # User exists. Now check password matches via the bcrypt
    # authenticate() method. If no match, then false else
    # method returns user object
    unless @user.nil?
      auth = @user.authenticate(params[:Password])
      if @user.authenticate(params[:Password])
        # add user id to session
        session[:user_id] = @user.id
        redirect_to "/users/#{@user.id}"
        return
      end
    end
    flash[:error] = "Profound apologies sir. Invalid data. Change it up and try again."
    redirect_to "/sessions/new"
  end

  # Logout User by removing :user_id from Session
  # Redirect to login page
  def destroy
    session[:user_id] = nil
    redirect_to '/sessions/new'
  end


end
