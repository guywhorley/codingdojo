class WallController < ApplicationController

  before_action :require_session_id, only: [:create_message, :index]
  def require_session_id
    unless session.has_key?(:id)
      redirect_to action: 'login'
    end
  end

  # Wall landing page, show messages and comments.
  def index
      # if !session.has_key?(:id)
      #     # need to login or register
      #     puts "In !session"
      #     redirect_to action: 'login'
      #     return
      # end
      @user = User.find(session[:id])
      @messages = Msg.all.order(created_at: :desc)
  end

  # process login
  def dologin
    begin
      user = User.find_by last_name: params[:last_name]
      if user.password == params[:password]
          session[:id] = user.id
          redirect_to action: 'index'
          return
      end
    rescue # user was not found.
    end
    flash[:alert] = "Sorry. Change some things and try again!"
    redirect_to '/wall/login'
  end

  # Create the new user
  def create
    begin
        @user = User.create(users_params)
        if @user.id
            session[:id] = @user.id
            redirect_to '/wall'
            return
        end
    rescue
    end
    flash[:alert] = "Sorry. Change some things and try again!"
    redirect_to '/wall/register'
  end

  # Create message
  def create_message
    # STOP USER-SPOOFING: Preventing user spoofing by moving hidden id field
    # out of form; getting value from session object instead.
    Msg.create(
      user_id: session[:id],
      message: params[:message])
    redirect_to '/wall'
  end

  # Show Login Page
  def login
  end

  # Logout
  def logout
      session[:id] = nil
      redirect_to action: 'index'
  end

  # Show Registration Page
  def register
  end

  private
     # rails 4.0 requires permission to let certion form field data to
     # pass to the model/dbase
     def users_params
        params.require(:user).permit(:last_name, :password)
     end

     def message_params
        params.permit(:user_id, :message)
     end


end
