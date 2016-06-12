class UsersController < ApplicationController
  def show
      @users = User.all
      render json: @users
  end

  def details
      # begin..rescue is a try..catch block
      # if record is not found, then error is raised.
      begin
          # parameters are availabe in the params hash
          @user = User.find(params[:id])
          render json: @user if @user
      rescue ActiveRecord::RecordNotFound
          render :text => "User ##{ params[:id] } not found!"
      end
  end

  def newUser
      redirect_to 'users/create'
  end

  def edit
      begin
          @user = User.find(params[:id])
          render 'edit.html.erb'
      rescue
          render :text => "User ##{ params[:id] } not found!"
      end
  end

  def total
      @count = User.count(:all)
      render :text => "User count: #{@count}"

  end

end
