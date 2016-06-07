# File: names.rb
# Author: Guy Whorley
# Iterate over array of hash names and print first_name, last_name

# Initialize Test Data
a = {:first_name => "Michael", :last_name => "Choi"}
b = {:first_name => "John", :last_name => "Supsupin"}
c = {:first_name => "KB", :last_name => "Tonel"}
d = {:first_name => "Jessie", :last_name => "De Leon"}
e = {:first_name => "Jaybee", :last_name => "Balog"}
names = [a, b, c, d, e]

# Iterate over array and print first and last name
def processNamesArray(arr)
    puts arr.to_s
    puts "You have #{arr.length} in the 'names' array"
    arr.each do |user|
        puts "The name is #{user.fetch(:first_name)} #{user.fetch(:last_name)}"
    end
end

########
# TEST
########
processNamesArray(names)
