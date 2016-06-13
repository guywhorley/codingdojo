class GameController < ApplicationController

  def index
    if !session.has_key?(:secret)
        session[:secret] = __initNumber()
        session[:allowreset] = "no"
    end
    @allowReset = session["allowreset"]

    render "index"
  end

  def guess

    # set player guess count to zero at game start
    if !session.has_key?(:guessCount)
        session[:guessCount] = 0
    end

    @allowReset = session['allowreset']

    # compare guess and secret number
    playerGuess = params[:guess].to_i
    secret = session[:secret].to_i
    puts "Secret: #{secret}, guess: #{playerGuess}"
    if (playerGuess == secret)
        flash[:notice] = "#{secret} was the number! Total Guesses: #{session[:guessCount]}"
        @allowReset = "yes"
    elsif (playerGuess < secret)
        flash[:alert] = "#{playerGuess} is too low!"

    else
        flash[:alert] = "#{playerGuess} is too high!"
    end

    session['allowreset'] = @allowReset
    # increment and save player guess count each time she guesses
    guessCount = session[:guessCount].to_i
    guessCount += 1
    session[:guessCount] = guessCount
    redirect_to root_path
  end

  # clear all game information: secret, guessCount,
  # and showResetButton
  def newgame
      session.clear
      redirect_to root_path
  end

  private

    def __initNumber(min=1, max=100)
        rand( (max-min) + min)
    end
end
