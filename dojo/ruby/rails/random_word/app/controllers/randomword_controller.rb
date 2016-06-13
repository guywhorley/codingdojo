class RandomwordController < ApplicationController

  def index
      if !session.has_key?(:count)
          session[:count] = 0
      end
      @count = session[:count].to_i
      @count += 1
      session[:count] = @count

      @rword = [*('a'..'z'),*('0'..'9')].shuffle[0,14].join.upcase


      render 'index'
  end
end
