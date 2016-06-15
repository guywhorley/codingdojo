class User < ActiveRecord::Base

    validates :first_name, :last_name, presence: true, length: { minimum: 2 }
    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
    validates :email_address, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
    validates :password, presence: true, length: { minimum: 8 }

    before_save do
       self.email_address.downcase!
     end

end
