class User < ActiveRecord::Base

    has_many :messages
    has_many :posts
    has_many :owners
    has_many :blogs, through: :owners
    has_many :comments, as: :commentable, dependent: :destroy 

end
