class SurveyController < ApplicationController

  def create
    if session.has_key?(:count)
    else
        session[:count] = 0
    end
    @count = session[:count].to_i
    @count += 1
    session[:count] = @count

    flash[:notice] = "Thanks for subitting this form. You have submitted this form #{@count} times."
    render 'result'
  end

  def result


  end

end
