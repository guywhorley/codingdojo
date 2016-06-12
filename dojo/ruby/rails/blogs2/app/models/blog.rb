class Blog < ActiveRecord::Base

    has_many :posts
    has_many :owners

    has_many :users, through: :owners
    has_many :comments, as: :commentable, dependent: :destroy



end
