# This is an implemention of various ciphers in Ruby
# Requires Ruby 2.x
# It uses Z = 26, or the Roman Alphabet for character input.

# Imports


# Global Constants
LETTERS = "abcdefghijklmnopqrstuvwxyz"
MY_DICT = Hash.new 
LETTERS.each_char.with_index { |character, index| MY_DICT[character] = index }


=begin
Clean all non-alphabetic characters from a string that are not in a provided list.

text - the original user-input text
keepchars - the string of characters that should be kept

Returns the full list of the character list.
=end
def clean_text(text, keepchars)
  cleaned_text = ''
  text.each_char { |character| cleaned_text += character if keepchars.include? character }
  cleaned_text.downcase!
  return cleaned_text
end


=begin
Translates an input key string to an integer array

key - the key, either a single character or string, to translate
mapping - the character to number hash
=end 
def translate_key(key, mapping)
  int_key = Array.new
  key.each_char do |char|
    if mapping.key?(char)
      int_key << mapping[char]
    end
  end
  return int_key
end


# Shift Cipher
def shift_cipher(key, text)
  ciphertext = ''
  encoded_text = Array.new
  key = translate_key(key, MY_DICT)
  message = clean_text(text, LETTERS)
  #puts message
  puts "Translated key is #{key}"
  puts "Key length is #{key.length}"
  message.each_char.with_index do |character, index|
    puts "Index is #{index}"
    puts "Key index is: " + (index % key.length).to_s
    encoded_text = MY_DICT[character]
    encrypted_text = (encoded_text + key[index % key.length]) % 26
    ciphertext += LETTERS[encrypted_text]
  end
  return ciphertext
end

# Substitution cipher

puts "Please provide some text: "
user_text = gets.chomp
#user_text.each_char { |character| puts MY_DICT[character] }
#user_text = clean_text(user_text, LETTERS)
puts "Text is: #{user_text}"

puts "Please provide a key: "
user_key = gets.chomp
#user_key = translate_key(user_key, MY_DICT)
puts "Key is: #{user_key}"

puts "The enciphered text is: " + shift_cipher(user_key, user_text)

