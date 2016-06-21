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

  def create
    @user = User.new(
      name: params[:name],
      email: params[:email],
      password: params[:password],
      password_confirmation: params[:password_confirmation]
    )
    if @user.valid?
      @user.save
      session[:user_id] = @user.id
      redirect_to "/users/#{@user.id}"
      return
    end
    flash[:errors] = @user.errors.full_messages
    redirect_to '/users/new'
  end

  def edit
    @user = User.find(params[:id])
  end

  def update
    user = User.update(params[:id],:name => params[:name],:email => params[:email],:password => params[:password],:password_confirmation => params[:password_confirmation])
    puts user.errors.full_messages

    redirect_to "/users/#{params[:id]}"
  end




end
