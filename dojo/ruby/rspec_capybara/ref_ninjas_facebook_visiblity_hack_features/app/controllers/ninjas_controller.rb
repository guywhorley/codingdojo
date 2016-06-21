class NinjasController < ApplicationController

    def new
    end

    def create
        ninja = Ninja.new(
            :ninja_name => params[:ninja_name],
            :ninja_description => params[:ninja_description]
        )
        if ninja.save
            redirect_to '/success'
        else
            # puts ninja.errors.full_messages.inspect
            flash[:error] = ninja.errors.full_messages
            render 'new'
        end
    end

    def success
        render :text => 'Form submitted succesfully!'
    end

end
