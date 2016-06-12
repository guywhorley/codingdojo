class Blog < ActiveRecord::Base
    has_many :blogs
    has_many :messages, through: :posts

    validates :name, :description, presence: true #, :last_name, length: { in: 2..20 }
    # validates :email_address, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
    # validates_numericality_of :age, greater_than: 10
    # validates_numericality_of :age, less_than: 150
end
