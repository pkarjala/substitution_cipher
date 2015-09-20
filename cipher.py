# This is a test for various ciphers in Python.
# Requires Python 3.x
# It uses Z = 26, or the Roman Alphabet for character input.

# Imports
import re

# LETTERS
LETTERS = "abcdefghijklmnopqrstuvwxyz"

# Character map
MYDICT = { LETTERS[i]:i for i in range(len(LETTERS)) }


def get_key(): # NOTE:  Does not check if character is a letter.
    print("\nPlease enter your key as a letter; i.e., a = b")
    key = input("> ")
    while len(key) > 1:
        print("\nKey length is greater than one letter; please", 
                "enter a single character key:")
        key = input("> ")
    return MYDICT[key]


def clean_text( text, keep_chars ):
    """Cleans a string of all characters not in a provided list.

    Takes the passed in string and translates it to lowercase, then removes
    all characters from the original string that are not also in the provided
    string keep_chars.

    Args:
        text: The text string to be cleaned.
        keep_chars: A string of the characters to keep.

    Returns:
        The original in-order string, stripped of all characters
            not in keep_chars.
    """
    cleantext = ''
    for character in text:
        if character in keep_chars:
            cleantext += character
    return cleantext



def shift_cipher(key, text):
    ciphertext = ''
    if key in MYDICT:
        key = MYDICT[key]
    print key
    message = clean_text(text, LETTERS)
    for character in message:
        encoded_text = MYDICT[character]
        encrypted_text = (encoded_text + key) % 26
        ciphertext += LETTERS[encrypted_text]
    # encoded_message = [MYDICT[i] for i in message]
    # encrypted_text = [(encoded_message[i] + key) % 26 for i in range(len(encoded_message))]
    # ciphertext = [LETTERS[i] for i in encrypted_text]
    return ciphertext



def mono_cipher(message, encode_or_decode):
    cyphertext = ''
    messagetext = ''
    message = message.lower()
    if encode_or_decode == 1:
        for character in message:
            encoded_text = MYDICT[character]
            encrypted_text = (encoded_text + key) % 26
            cyphertext += LETTERS[encrypted_text]
        return cyphertext.upper()
    elif encode_or_decode == 2:
        for character in message:
            encoded_text = MYDICT[character]
            decrypted_text = (encoded_text - key) % 26
            messagetext += LETTERS[decrypted_text]
        return messagetext.lower()



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