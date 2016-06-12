class Character < ActiveRecord::Base
  belongs_to :house

  def isLord?
      if House.find_by(lord: self)
          return true
      end
      return false
    
  end
end
