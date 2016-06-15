class WallController < ApplicationController

  def index
      if !session[:id]
          # need to login or register
          puts "In !session"
          render 'login'
      end
  end

  def create
    @user = User.create(:name params["last_name"], password: params['password'])
    render :text => 'creating user'

  end

  private
     # rails 4.0 requires permission to let certion form field data to
     # pass to the model/dbase
     def users_params
        params.require(:user).permit(:last_name, :password, :id)
     end


end
