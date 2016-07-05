class User < ActiveRecord::Base

    validates :last_name, :password, presence: true
    validates :last_name, uniqueness: true,  length: { minimum: 2 }
    validates :password, length: { minimum: 3 }

end
