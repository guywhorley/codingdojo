class SessionsController < ApplicationController

  def new

    if session.key?(:user_id)
      redirect_to "/users/#{session[:user_id]}"
      return
    end


  end

  def create
    # Initially, find the user by email. If exists, then check
    # for matching password via bcrypt
      # puts "create- params #{params.inspect}"
    @user = User.find_by email: params[:Email]
      # puts "@user = #{@user}"

    # User exists. Now check password matches via the bcrypt
    # authenticate() method. If no match, then false else
    # method returns user object
    unless @user.nil?
      auth = @user.authenticate(params[:Password])
        # puts "User Auth: #{auth}"

      if @user.authenticate(params[:Password])
        # puts "User password authenticated."
        # add user id to session
        session[:user_id] = @user.id
        redirect_to "/users/#{@user.id}"
        return
      end
      flash[:error] = "User exists - failed password authentication!"
      redirect_to "/sessions/new"
      return
    end
    flash[:error] = "Unable to find user by email."
    redirect_to "/sessions/new"
  end

  # Logout User by removing :user_id from Session
  # Redirect to login page
  def destroy
    session[:user_id] = nil
    redirect_to '/sessions/new'
  end


end
