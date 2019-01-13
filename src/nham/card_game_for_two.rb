number_of_card = gets.chomp
cards = gets.chomp

number_of_card = number_of_card.to_i # Not use
cards = cards.strip
cards.sub!(/\s+/, " ")
cards = cards.split(" ")
cards.map!{ |x| x.to_i }
cards = cards.sort.reverse
alice_score = 0
bod_score = 0
cards.each_with_index do |card, index|
  if index % 2 == 0
    alice_score += card
  else
    bod_score += card
  end
end
puts "#{alice_score - bod_score}"
