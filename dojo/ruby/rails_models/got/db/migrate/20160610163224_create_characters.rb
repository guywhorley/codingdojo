class CreateCharacters < ActiveRecord::Migration
  def change
    create_table :characters do |t|
      t.string :name
      t.integer :age
      t.boolean :gender
      t.references :house, index: true, foreign_key: true
      t.boolean :dead

      t.timestamps null: false
    end
  end
end
