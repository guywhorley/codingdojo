class ProductsController < ApplicationController

  # show all beer
  def index
      @products = Product.all.order(:name)
  end

  # show new beer page
  def new
  end

  # add beer to the db
  def create
      Product.create(allow_params)
      redirect_to '/products'
  end

  # show beer details
  def show
      @beer = Product.find(params[:id])
  end

  # edit beer details
  def edit
      @beer = Product.find(params[:id])
  end

  # update the beer entry
  def update
      Product.find(params[:id]).update(allow_params)
      redirect_to '/products'
  end

  # destroy
  def destroy
      Product.find(params[:id]).destroy
      redirect_to '/products'
  end


  private
        def allow_params
            params.require(:product).permit(:id, :name, :description, :pricing)
        end
end
