class AddSomeColumns < ActiveRecord::Migration
  def change

       add_column :ninjas, :some_column, :string
       add_column :ninjas, :another_column, :string
      
  end
end
