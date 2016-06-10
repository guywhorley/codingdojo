class Dojo < ActiveRecord::Base

    # this relationship causes Rails to automatically delete
    # any records in the Ninja table that are related to any
    # Dojo upon deletion of that Dojo
    has_many :Ninjas, :dependent => :destroy

    validates :name, :city, :state, presence: true
    validates :state, length: { in: 2..2 }



    # validates :first_name, :last_name, length: { in: 2..20 }
    # validates :email_address, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
    # validates_numericality_of :age, greater_than: 10
    # validates_numericality_of :age, less_than: 150
    #
    # # before_save do
    # # end
end
