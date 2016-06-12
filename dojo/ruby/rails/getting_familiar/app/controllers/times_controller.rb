class TimesController < ApplicationController

    def index

        #check for existing session, add if missing
        if !session.has_key?("count")
            session['count'] = 0
        end

    # get session count, increment, save
    @count = session['count'].to_i
    @count += 1
    session['count'] = @count.to_s

    render :text => "You visited the site #{@count} times!"
    end

    def restart
        session.clear
        render :text => "Destroy the session!"

    end

end #class
