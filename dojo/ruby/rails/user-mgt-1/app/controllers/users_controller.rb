class UsersController < ApplicationController
  def index
      @users = User.all
      puts (@users.to_s)
      render "index"
  end

  def new
      render 'newuser'
  end

  def show
      @user = User.find(params[:id])
  end

  def create
      User.create(users_params)
      redirect_to action: "index" #this is how to redirect to the index action
  end

  def edit
      # puts "Method: #{params['_method']}"
      if params["_method"] == "destroy"
          User.find(params[:id]).destroy
          redirect_to action: "index"
      else
         @user = User.find(params[:id])
         render "edit"
      end
  end

  def update
      User.find(params[:id]).update(users_params)
      redirect_to action: "index"
  end


  private
     # rails 4.0 requires permission to let certion form field data to
     # pass to the model/dbase
     def users_params
        params.require(:user).permit(:first_name, :last_name, :email_address, :password, :id)
     end

end
