var_ab = gets.chomp
var_ab = var_ab.strip
var_ab.sub!(/\s+/, " ")
var_a = var_ab.split(" ")[0].to_i
var_b = var_ab.split(" ")[1].to_i

puts "#{((var_a * var_b) % 2 == 0)? 'Even' : 'Odd'}"
