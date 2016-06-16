class CreateMathdojos < ActiveRecord::Migration
  def change
    create_table :mathdojos do |t|

      t.timestamps null: false
    end
  end
end
