class SayController < ApplicationController

    def index
        render :text => "What do you want me to say?"

    end

    def sayHello
        render :text => "Saying Hello!"
    end

    def joe
        render :text => "Saying Hello Joe!"
    end

end
