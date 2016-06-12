class CreateComments < ActiveRecord::Migration
  def change
    create_table :comments do |t|
      t.string :name
      t.references :commentable, polymorphic: true, index: true

      t.timestamps null: false
    end
    add_index :comments, :name
  end
end
