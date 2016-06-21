class RemoveExtraColumns < ActiveRecord::Migration
  def change
     remove_column :ninjas, :some_column
     remove_column :ninjas, :another_column
  end
end
