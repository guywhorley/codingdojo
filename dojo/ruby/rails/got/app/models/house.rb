class House < ActiveRecord::Base
  belongs_to :lord, :class_name => 'Character'
  has_many :characters
end
