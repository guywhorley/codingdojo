class UsersController < ApplicationController

    def new
    end

    def create
        @user = User.create(
            :first_name => params[:first_name],
            :last_name => params[:last_name],
            :email => params[:email],
            :password => params[:password],
            :password_confirmation => params[:password_confirmation]
        )
        # puts "error messages: #{@user.errors.full_messages.join(',')}"
        if @user.errors.full_messages.length > 0
            render :text => "Unable to register!"
        else
            render :text => "Success"
        end
    end

end
