class AnimesController < ApplicationController

    # landing page - show all animes in the db
    def index
        if !session[:count]
            session[:count] = 0
        end
        session[:count] += 1
        @pets = Pet.all
    end

    # invoke 'create new anime' form
    def create
        Pet.create(my_params)
        redirect_to '/animes'
    end

    # show details
    def show
        @pet = Pet.find(params[:id])
    end
    # edit the pet
    def edit
        @pet = Pet.find(params[:id])
    end

    # Update the Pet
    def update
        pet = Pet.find(params[:id])
        pet.name = params[:name]
        pet.save
        redirect_to '/animes'
    end

    def destroy
        Pet.find(params[:id]).destroy
        redirect_to '/animes'
    end

    private
       # rails 4.0 requires permission to let certion form field data to
       # pass to the model/dbase
       def my_params
          params.require(:pet).permit(:id, :name)
       end
end
