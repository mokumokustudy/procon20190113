number_of_number = gets.chomp
list_numbers = gets.chomp
number_of_number = number_of_number.to_i # Not use this variable
list_numbers = list_numbers.strip
list_numbers.sub!(/\s+/, " ")
list_numbers = list_numbers.split(" ")
list_numbers.map!{ |x| x.to_i }
counter = 0
while list_numbers.select { |x| x % 2 == 1}.empty? do
  list_numbers.map! { |x| x/2 }
  counter += 1
end
puts counter
