class User < ActiveRecord::Base

# Add Validations here

    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

    validates :first_name, :last_name, :age, presence: true
    validates :first_name, :last_name, length: { in: 2..20 }
    validates :email_address, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
    validates_numericality_of :age, greater_than: 10
    validates_numericality_of :age, less_than: 150

    before_save do
        self.email_address.downcase!
    end

end
