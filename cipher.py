# This is a test for various ciphers in Python.
# It uses Z = 26, or the Roman Alphabet for character input.

# Imports
import re

# Character map
char_map = { 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
rev_map = dict ( zip( char_map.values(), char_map.keys() ) )

def get_key():
	print( "\nPlease enter your key as a letter; i.e., a = b" )
	key = input( "> " )
	while len(key) > 1:
		print( "\nKey length is greater than one letter; please enter a single character key:")
		key = input( "> " )
	return char_map[key]

def mono_cipher(message, enc_or_dec):
	cyphertext = ''
	messagetext = ''
	message = message.lower()
	if enc_or_dec == 1:
		for character in message:
			encoded_text = char_map[character]
			encrypted_text = (encoded_text + key) % 26
			cyphertext += rev_map[encrypted_text]
		return cyphertext.upper()

	elif enc_or_dec == 2:
		for character in message:
			encoded_text = char_map[character]
			decrypted_text = (encoded_text - key) % 26
			messagetext += rev_map[decrypted_text]
		return messagetext.lower()


print( "\n\nPlease select a Substitution Cipher to use:" )

cipher = int(input("Monoalphabetic [1]; Polyalphabetic [2]; Affine [3] \n> "))

if cipher == 1:
	print( "\nMonoalphabetic cipher chosen.\n" )
	repeat = True
	while repeat:
		enc_or_dec = int(input("Encipher [1] or Decipher [2] \n> "))
		key = get_key()
		print( "\nKey is " + str(key) )
		print( "\nPlease enter your message to be encrypted:" ) if enc_or_dec == 1 else print( "\nPlease enter your message to be decrypted:")
		message = input("> ")
		message = re.sub(r'\s+', '', message)
		result = mono_cipher(message, enc_or_dec)
		print( "\nEncrypted message is: " + result ) if enc_or_dec == 1 else print( "\nDecrypted message is: " + result )

		print( "Do you wish to perform another Monoalphabetic cipher task?")

		repeat = False
		# elif enc_or_dec == 2:
		# 	key = get_key()
		# 	print( "\nKey is " + str(key) )
		# 	print( "\nPlease enter your message to be decrypted:")
		# 	message = input("> ")
		# 	message = re.sub(r'\s+', '', message)
		# 	message = message.lower()
		# 	for character in message:
		# 		enc_text = char_map[character]
		# 		decrypted_text = enc_text - key % 26
		# 		plaintext += rev_map[decrypted_text]
		# 	print( "\nDecrypted message is: " + plaintext.upper() )

		# 	print( "Do you wish to perform another Monoalphabetic cipher task?")

		# 	repeat = False
elif cipher == 2:
	print( "Polyalphabetic cipher chosen.")
elif cipher == 3:
	print( "Affine cipher chosen.")
else:
	print( "Sorry; a valid choice was not made. Exiting...")
