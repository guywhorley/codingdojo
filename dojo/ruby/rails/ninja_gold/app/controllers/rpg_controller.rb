class RpgController < ApplicationController
  def index
      if !session.has_key? (:venue)
          __initGame
      end
      @gold = session[:playerGold]
  end


  def processTurn
      balance = session[:playerGold].to_i
      gold = 0
      if params[:venue] == "farm"
          gold = __rndRange(10, 20)
      elsif params[:venue] == "cave"
          gold = __rndRange(5,10)
      elsif params[:venue] == "house"
          gold = __rndRange(2,5)
      else # casino
          gold = __rndRange(-50,50)
      end
      __logMessage(params[:venue], gold)
      balance += gold
      session[:playerGold] = balance
      redirect_to "/"
  end

  def playAgain
      session.clear
      redirect_to "/"
  end

  private

    def __initGame
        session[:venue] = "na"
        session[:playerGold] = 0
        session[:log] = []
    end

    def __logMessage(venue, gold)
        message_arr = []
        message_arr = session[:log]
        message_hash = {} # build a single message

        # format time
        now = Time.now.strftime("%b  %d, %Y at %k:%M")
        puts "Time: #{now}"
        if gold >= 0
            message_hash = {
                "type": "notice",
                "message": "Earned #{gold} gold from the #{venue}!  (#{now})"
            }
        else
            message_hash = {
                "type": "alert",
                "message": "Entered a #{venue} and lost #{gold} gold... Ouch!  (#{now})"
            }
        end
        message_arr.insert(0, message_hash)
        session[:log] = message_arr
        puts message_arr.inspect
    end

    def __rndRange(min, max)
        rnd = Random.new
        num = 0
        if (min < 0 && max < 0)
            absMax = max.abs + 1
            absMin = min.abs
            num = -(rnd.rand(absMax - absMin) + absMin)
        elsif (min >= 0 && max >=0)
            max += 1
            num = rnd.rand(max - min) + min
        elsif (min <0 && max > 0)
            relZero = min.abs
            relMax = max + relZero + 1
            relNum = rnd.rand((relMax))
            num = (relNum - relZero)
        end
        num
    end
end
