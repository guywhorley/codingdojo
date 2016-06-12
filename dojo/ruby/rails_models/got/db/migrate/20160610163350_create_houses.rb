class CreateHouses < ActiveRecord::Migration
  def change
    create_table :houses do |t|
      t.string :name
      t.string :location
      t.references :lord, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
