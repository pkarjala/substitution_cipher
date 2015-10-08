# This is an implemention of various ciphers in Ruby
# Requires Ruby 2.x
# It uses Z = 26, or the Roman Alphabet for character input.

# Imports


# Global Constants
LETTERS = "abcdefghijklmnopqrstuvwxyz"
MY_DICT = Hash.new 
LETTERS.each_char.with_index { |character, index| MY_DICT[character] = index }



# Clean all non-alphabetic characters from a string that are not in a provided list.
#
# @param text [String] The original user-input text.
# @param keepchars [String] The string of characters that should be kept.
#
# @return [String] The original text cleaned of all characters not in keepchars,
#   and in lowercase.
def clean_text(text, keepchars)
  cleaned_text = ''
  text.each_char { |character| cleaned_text += character if keepchars.include? character }
  cleaned_text.downcase!
  return cleaned_text
end


# Translates an input key string to an integer array
#
# @param key [String] The key, either a single character or string, to translate.
# @param mapping [Map] The character to number hash table.
#
# @return [Array] The key array as integers.
def translate_key(key, mapping)
  int_key = Array.new
  key.each_char do |character|
    if mapping.key?(character)
      int_key << mapping[character]
    end
  end
  return int_key
end


# Performs shift cipher against any length key.
#
# @param key [String] the key, in plain text, of any length.
# @param text [String] the plaintext, of any length, inclusive of incorrect characters.
#
# @return [String] Returns the encrypted ciphertext.
def shift_cipher(key, text)
  ciphertext = ''
  encoded_text = ''
  key = translate_key(key, MY_DICT)
  message = clean_text(text, LETTERS)
  message.each_char.with_index do |character, index|
    encoded_text = MY_DICT[character]
    encrypted_text = (encoded_text + key[index % key.length]) % 26
    ciphertext += LETTERS[encrypted_text]
  end
  return ciphertext
end

# Performs shift decipher against any length key.
#
# @param key [String] the key, in plain text, of any length.
# @param text [String] the ciphertext, of any length.
#
# @return [String] Returns the decrypted plaintext.
def shift_decipher(key, text)
  plaintext = ''
  encoded_text = ''
  key = translate_key(key, MY_DICT)
  ciphertext = clean_text(text, LETTERS)
  ciphertext.each_char.with_index do |character, index|
    encoded_text = MY_DICT[character]
    encrypted_text = (encoded_text - key[index % key.length]) % 26
    plaintext += LETTERS[encrypted_text]
  end
  return plaintext
end


