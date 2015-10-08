# Use this file for testing algorithms in the cipher file
require_relative 'cipher'

puts "Please provide some text: "
user_text = gets.chomp
#user_text.each_char { |character| puts MY_DICT[character] }
#user_text = clean_text(user_text, LETTERS)
puts "Text is: #{user_text}"

puts "Please provide a key: "
user_key = gets.chomp
#user_key = translate_key(user_key, MY_DICT)
puts "Key is: #{user_key}"

ciphertext = shift_cipher(user_key, user_text)

puts "The enciphered text is: " + ciphertext

deciphertext = shift_decipher(user_key, ciphertext)

puts "The deciphered text is: " + deciphertext