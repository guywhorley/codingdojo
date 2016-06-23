class SecretsController < ApplicationController

  before_action :require_login, only: [:new, :create, :destroy, :index]

  def index
    # it is nec' to get current user and store in the @user so that the header
    # <% %> on app layout can figure out if logout needs to be displayed.
    @user = current_user
    @secrets = Secret.all
  end

  def create
    # puts "PARAMS: #{params.inspect}"
    @user = current_user
    secret = @user.secrets.create(
      content: params[:NewSecret],
      user_id: @user.id
    )

    # puts @user.errors.messages.inspect
    redirect_to "/users/#{session[:user_id]}"
  end

  def destroy
    Secret.find(params[:id]).delete
    redirect_to "/users/#{session[:user_id]}"
    # redirect_to "/secrets"
  end

end
