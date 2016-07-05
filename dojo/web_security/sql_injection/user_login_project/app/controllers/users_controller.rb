class UsersController < ApplicationController
  def index
  end

  def create
    user = User.where("email_address = '#{params[:email_address]}'")
    puts "User: #{user.to_s}"

    # ESCAPING USER INPUT
    # The following format is SANITIZED --- any special chars are escaped through string interpolation.
    # NEVER PASS DIRECT USER INPUT INTO A SQL STATEMENT!!!  !!!   !!!!

    # Approach #1: Inline Interpolation
    if User.where("email_address = ? AND password = ?", params[:email_address], params[:password])
       render :text => "Congratulations! You are now in."
    else
       render :text => "You have provided a wrong email"
    end

    # Approach #2: User Input Interpoated into a Hash
    User.where("email_address = :email AND password = :pwd",
        { email: params[:email_address], pwd: params[:password]} )


    # User.update(User.last.id, :email_address => params[:email])
  end
end
