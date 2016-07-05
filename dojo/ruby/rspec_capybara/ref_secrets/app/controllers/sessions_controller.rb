class SessionsController < ApplicationController

  def create
    # Initially, find the user by email. If exists, then check
    # for matching password via bcrypt
      # puts "create- params #{params.inspect}"
    @user = User.find_by email: params[:login_username]
      # puts "@user = #{@user}"

    # User exists. Now check password matches via the bcrypt
    # authenticate() method. If no match, then false else
    # method returns user object
    unless @user.nil?
      # auth = @user.authenticate(params[:login_password])
        # puts "User Auth: #{auth}"

      if @user.authenticate(params[:login_password])
        # puts "User password authenticated."
        # add user id to session
        session[:user_id] = @user.id
        redirect_to "/auctions"
        return
      end
      flash[:error] = "Ruh Roh! Try again."
      redirect_to "/sessions"
      return
    end
    flash[:error] = "Ruh Roh! Try again."
    redirect_to root_path #{ }"/sessions/new"
  end

  # Logout User by removing :user_id from Session
  # Redirect to login page
  def destroy
    session[:user_id] = nil
    redirect_to '/sessions/new'
  end


end
