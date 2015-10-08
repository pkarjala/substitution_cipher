# Use this file for testing algorithms in the cipher file
require_relative 'cipher'

puts "Please provide some text: "
user_text = gets.chomp
#user_text.each_char { |character| puts MY_DICT[character] }
#user_text = clean_text(user_text, LETTERS)
puts "Text is: #{user_text}"

puts "Please provide key 1: "
user_key1 = gets.chomp
#user_key = translate_key(user_key, MY_DICT)
puts "Key is: #{user_key1}"

puts "Please provide key 2: "
user_key2 = gets.chomp
#user_key = translate_key(user_key, MY_DICT)
puts "Key is: #{user_key2}"

deciphertext = affine_decipher(user_key1, user_key2, user_text)

#ciphertext = shift_cipher(user_key1, user_text)

# puts "The enciphered text is: " + ciphertext

puts "The deciphered text is: " + deciphertext

# deciphertext = shift_decipher(user_key, ciphertext)

# puts "The deciphered text is: " + deciphertext

# puts extended_euclidian_algorithm(26, 11)

