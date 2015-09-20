# This is a test for various ciphers in Python.
# Requires Python 3.x
# It uses Z = 26, or the Roman Alphabet for character input.

# Imports
import re

# Letters
letters = "abcdefghijklmnopqrstuvwxyz"

# Character map
mydict = { letters[i]:i for i in range(len(letters)) }

def get_key(): # NOTE:  Does not check if character is a letter.
    print("\nPlease enter your key as a letter; i.e., a = b")
    key = input("> ")
    while len(key) > 1:
        print("\nKey length is greater than one letter; please", 
                "enter a single character key:")
        key = input("> ")
    return mydict[key]

# clean_text
# PAK 20150919
# Remove all non-alphabetic characters, spaces, and other puncutation from text.
# @param text The Text to be cleaned.
# @return A string of characters {a...z} in lowercase
def clean_text( text ):
    cleantext = ''
    for character in text:
        if mydict[character] :
            cleantext += character
    return cleantext


def mono_cipher(message, encode_or_decode):
    cyphertext = ''
    messagetext = ''
    message = message.lower()
    if encode_or_decode == 1:
        for character in message:
            encoded_text = mydict[character]
            encrypted_text = (encoded_text + key) % 26
            cyphertext += letters[encrypted_text]
        return cyphertext.upper()
    elif encode_or_decode == 2:
        for character in message:
            encoded_text = mydict[character]
            decrypted_text = (encoded_text - key) % 26
            messagetext += letters[decrypted_text]
        return messagetext.lower()

def monoalpha_encode(message):
    ciphertext = ''
    message = clean_text(message)

print("\n\nPlease select a Substitution Cipher to use:")

cipher_type = int(input("Monoalphabetic [1]; Polyalphabetic [2]; Affine [3] \n> "))

if cipher_type == 1:
    print("\nMonoalphabetic cipher chosen.\n")
    repeat = True
    while repeat:
        encode_or_decode = int(input("Encipher [1] or Decipher [2] \n> "))
        key = get_key()
        print("\nKey is " + str(key))
        print("\nPlease enter your message to be encrypted:") if encode_or_decode == 1 else print("\nPlease enter your message to be decrypted:")
        message = input("> ")
        message = re.sub(r'\s+', '', message)
        result = mono_cipher( message, encode_or_decode )
        print("\nEncrypted message is: " + result) if encode_or_decode == 1 else print("\nDecrypted message is: " + result)

        # To be broken out into separate management function
        print("\nDo you wish to perform another Monoalphabetic cipher task?")
        print("[Y]es | [N]o")
        another = input("> ")
        while(another not in ('y', 'Y', 'n', 'N')):
            print("\nSorry, your input is not valid; do you wish to perform ",
                  "another cipher task?")
            print("[Y]es | [N]o")
            another = input("> ")

        if another in ('n', 'N'):
            repeat = False 
        else :
            repeat = True

elif cipher_type == 2:
    print("\nPolyalphabetic cipher chosen.\n")
    # To be added
elif cipher_type == 3:
    print("\nAffine cipher chosen.\n")
    # To be added
else:
    print("\nSorry; a valid choice was not made.\n")