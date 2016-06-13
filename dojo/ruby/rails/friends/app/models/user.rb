class User < ActiveRecord::Base
    # order is important, linking table must first be defined.

    has_many :friendships
    has_many :friends, through: :friendships

    belongs_to :friends,
        class_name: "User",
        foreign_key: "friend_id"
end
