class UsersController < ApplicationController

  before_action :require_login, except: [:new, :create]
  
  def index
    # # :id is passed from session controller in URL, lookup user
    # # and pass into view
    # @user = User.find_by(id: params[:id])
    redirect_to "/show/#{session[:user_id]}"
  end

  def show
    # :id is passed from session controller in URL, lookup user
    # and pass into view
  @user = User.find_by(id: params[:id])
  @secrets = @user.secrets
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
    flash[:error] = "Uh oh. Change values and try again!" #@user.errors.full_messages
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

  def destroy
    puts "destroy: id=#{params[:id]}"
    user = User.find(params[:id])
    user.secrets.delete
    user.delete
    # User.delete(params[:id].to_i) # MUST CONVERT FROM STRING ON FORM TO INTEGER FOR DELETE METHOD
    session[:user_id] = nil
    redirect_to ('/sessions/new')
  end

end
