class Ninja < ActiveRecord::Base

    # require all fields be present
    validates :ninja_name, :ninja_description, :presence => true
    validates :ninja_name, :ninja_description, :length => { :minimum => 2 }

end
