class TimesController < ApplicationController
  def main
      @dateNow = Time.now.strftime("%b %-d, %Y")
      @timeNow = Time.now.strftime("%l:%M %p")

  end
end
