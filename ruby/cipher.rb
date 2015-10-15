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
  text.downcase!
  cleaned_text = ''
  text.each_char { |character| cleaned_text += character if keepchars.include? character }
  return cleaned_text
end


# Translates an input key string to an integer array
#
# @param key [Array] The key, either a single character or string, to translate.
# @param mapping [Map] The character to number hash table.
#
# @return [Array] The key array as integers.
# NOTE:  Chokes on plain integer input; test.
def translate_key(key, mapping)
  int_key = Array.new
  key.each do |item|
    if mapping.key?(item)
      int_key << mapping[item]
    else
      int_key << item
    end
  end
  return int_key
end


# Performs Shift Cipher against any key length >= 1.
#
# @param key [Array] the key as an array of any combination of integers and characters.
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

# Performs Shift Decipher against any key length >= 1.
#
# @param key [Array] the key as an array of any combination of integers and characters.
# @param text [String] the ciphertext, of any length.
#
# @return [String] Returns the decrypted plaintext.
def shift_decipher(key, text)
  plaintext = ''
  encrypted_text = ''
  key = translate_key(key, MY_DICT)
  ciphertext = clean_text(text, LETTERS)
  ciphertext.each_char.with_index do |character, index|
    encrypted_text = MY_DICT[character]
    encoded_text = (encrypted_text - key[index % key.length]) % 26
    plaintext += LETTERS[encoded_text]
  end
  return plaintext
end


# Performs the extended euclidian algorithm to find the GCD of two numbers.
# 
# @param a [Integer] The first number.
# @param b [Integer] The second number.
#
# @return [Array] The GCD of the two numbers, along with the final s & t values.
def extended_euclidian_algorithm(a,b)
  r0 = ''
  r1 = ''
  r0 = a
  r1 = b
  s0 = 1
  s1 = 0
  t0 = 0
  t1 = 1
  q = ''
  temp = ''
  while r1 != 0
    q = (r0 / r1).floor
    temp = r0
    r0 = r1
    r1 = temp - q * r1
    temp = s0
    s0 = s1
    s1 = temp - q * s1
    temp = t0
    t0 = t1
    t1 = temp - q * t1
  end
  d = r0
  return [d, s0, t0]
end


# Performs an Affine Cipher against any two part key, where key length >=1.
# 
# Calculates A * m + B % 26
#
# @param key1 [Array] The first part of the key A as an array of any combination 
#   of integers and characters.
# @param key2 [String] The second part of the key B as an array of any combination 
#   of integers and characters.
#
# @return [String} The enciphered text string.
def affine_cipher(key1, key2, text)
  ciphertext = ''
  encoded_text = ''
  a = translate_key(key1, MY_DICT)
  b = translate_key(key2, MY_DICT)
  message = clean_text(text, LETTERS)
  message.each_char.with_index do |character, index|
    encoded_text = MY_DICT[character]
    encrypted_text = (encoded_text * a[index % a.length] + b[index % b.length]) % 26
    ciphertext += LETTERS[encrypted_text]
  end
  return ciphertext
end


# Performs an Affine Cipher against any two part key, where key length >=1.
# 
# Calculates 1/A * (c - B) % 26
#
# @param key1 [Array] The first part of the key A as an array of any combination 
#   of integers and characters.
# @param key2 [String] The second part of the key B as an array of any combination 
#   of integers and characters.
#
# @return [String] The deciphered text string.
def affine_decipher(key1, key2, text)
  plaintext = ''
  encrypted_text = ''
  a1 = Array.new
  a = translate_key(key1, MY_DICT)
  b = translate_key(key2, MY_DICT)
  a.each do |value|
    gcd = extended_euclidian_algorithm(26, value)
    a1 << gcd[2] % 26
  end
  ciphertext = clean_text(text, LETTERS)
  ciphertext.each_char.with_index do |character, index|
    encrypted_text = MY_DICT[character]
    encoded_text = (encrypted_text * a1[index % a1.length] - a1[index % a1.length]*b[index % b.length]) % 26
    plaintext += LETTERS[encoded_text]
  end
  return plaintext
end


# Performs a frequency analysis on a provided string of characters.
#
# Calculates the relative frequency of each character in the overall string.
#
# @param text [String] The unaltered string to count characters of.
#
# @return [Array] The mapping of the frequency of each character.
def frequency_analysis(text)
  frequency_table = {}
  for key in 'a'..'z' do 
    frequency_table[key] = 0
  end
  text = clean_text(text, LETTERS)
  text.each_char do |character|
    frequency_table[character] += 1
  end
  relative_frequency = {}
  frequency_table.each { |key, value| 
    relative_frequency[key] = (value * 100.0) / text.length
  }
  result = relative_frequency.sort_by { |_key, value| value }
  result.reverse!
  return result
end


# Decodes a message based on any partial provision of mappings
#
# @param text [String] The message to be deciphered.
# @param mapping [Hash] A mapping of any number or characters in Z26 to Z26
#
# @return [String] The text of deciphered characters, with "_" for any characters
#   not deciphered.  Any non {a..z} letters are simply passed through.
def decode_mapping(text, mapping)
  result_text = ''
  text.downcase!
  text.each_char do |character|
    if mapping.key?(character)
      result_text << mapping[character]
    else
      if LETTERS.include? character
        result_text << "_"
      else
        result_text << character
      end
    end
  end
  return result_text
end