class Post < ActiveRecord::Base
  belongs_to :blog
  belongs_to :user

  has_many :messages
  has_many :owners, through: :blogs
  has_many :users, through: :messages
  has_many :comments, as: :commentable, dependent: :destroy

end
