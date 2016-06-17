class User < ActiveRecord::Base

    # require all fields be present
    validates :first_name, :last_name, :password, :presence => true
    validates :first_name, :last_name, :length => { :minimum => 2 }

    # require valid email format
    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
    validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }

    # require passwords match and be at least 6 chars long
    validates :password, :confirmation => true
    validates :password, :length => { :minimum => 6 ,
              :message => "Password must be at least 6 characters long" }

    before_save do
        self.email.downcase!
    end

end
