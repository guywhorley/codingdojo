class ProductsController < ApplicationController

    def index
    #   if errors?
    #       flash[:error] = "You have errors"
    #   redirect_to '/users/' #pathing will be explained later
    # else
    #   flash[:success] = "You did it!"
    #   redirect_to '/users/'
    # end
      @products = Product.all
      # puts json: @products
      # render :text => "at index" # json: @products
      
      # implicit or automatic rendering, 'convention over configuration'f
    end

    def create
      @product = Product.create(name: params[:name], description: params[:description])

      #adds the value in params[:id] to the :id key in session
      session[:id] = params[:id] #we will talk about params in a bit

      redirect_to '/products/index'
    end

    # def log_out
    #   #sets the session[:id] to nil, overwriting the previous value
    #   session[:id] = nil
    #   #session.clear
    #   #reset_session
    # end

end
