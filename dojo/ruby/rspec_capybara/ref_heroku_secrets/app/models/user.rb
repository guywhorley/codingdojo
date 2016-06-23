class User < ActiveRecord::Base

  has_secure_password  # compares AND hashes

  # validations
  validates :name, :password, :password_confirmation, :presence => true
  validates :name, :length => { :minimum => 2 }
  validates :password, :confirmation => true

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }

  # relationships
  has_many :secrets
  has_many :likes, dependent: :destroy
  has_many :secrets_liked, through: :likes, source: :secret
  
  # callbacks
  before_save do
    self.email.downcase!
  end

end
