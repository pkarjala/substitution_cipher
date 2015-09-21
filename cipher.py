# This is a test for various ciphers in Python.
# Requires Python 3.x
# It uses Z = 26, or the Roman Alphabet for character input.

# LETTERS
LETTERS = "abcdefghijklmnopqrstuvwxyz"

# Character map of letters to number
MYDICT = { LETTERS[i]:i for i in range(len(LETTERS)) }


def get_key():
    """ Gets a key from the user.

    Key must be of a length of only one character.

    Args:
        none

    Returns:
        The key input by the user.
    """
    print("\nPlease enter your key as a letter; i.e., a = b")
    key = input("> ")
    while len(key) > 1:
        print("\nKey length is greater than one letter; please", 
                "enter a single character key:")
        key = input("> ")
    return key


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
    text = text.lower()
    for character in text:
        if character in keep_chars:
            cleantext += character
    return cleantext


def translate_key(key, mapping):
    """Translates a key from a character to an integer.


    Args:
        key:  The key to translate.

    Returns:
        The key as an integer.

    """
    if key in mapping:
        key = mapping[key]
    print(key)
    return key


def shift_cipher(key, text):
    """Performs shift cipher on a string based off of a key provided.

    Performs a shift cipher, key + text % 26 to encipher.

    Args:
        key:  The key to shift the text over by.  May be either the text of the
            letter or the number of the letter.
        text:  The plaintext to encipher.  Will be stripped of non-alphabetic
            characters before being enciphered.

    Returns:
        The enciphered plaintext

    """
    ciphertext = ''
    key = translate_key(key, MYDICT)
    message = clean_text(text, LETTERS)
    for character in message:
        encoded_text = MYDICT[character]
        encrypted_text = (encoded_text + key) % 26
        ciphertext += LETTERS[encrypted_text]
    return ciphertext


def shift_decipher(key, text):
    """Performs shift decipher on a string based off of a key provided.

    Performs a shift decipher, key - text % 26 to decipher the enciphered text.

    Args:
        key:  The key to shift the text over by.  May be either the text of the
            letter or the number of the letter.
        text:  The ciphertext to decipher.  Will be stripped of non-alphabetic
            characters before being deciphered.

    Returns:
        The deciphered plaintext

    """
    plaintext = ''
    key = translate_key(key, MYDICT)
    ciphertext = clean_text(text, LETTERS)
    for character in ciphertext:
        encrypted_text = MYDICT[character]
        encoded_text = (encrypted_text - key) % 26
        plaintext += LETTERS[encoded_text]
    return plaintext


def affine_cipher(key, text):
    ciphertext = ''
    a = translate_key(key[0], MYDICT)
    b = translate_key(key[1], MYDICT)
    message = clean_text(text, LETTERS)
    for character in message:
        encoded_text = MYDICT[character]
        encrypted_text = (encoded_text * a + b) % 26
        ciphertext += LETTERS[encrypted_text]
    return ciphertext

def affine_decipher(key, text):
    plaintext = ''
    kfor part in key:
        key[part] = translate_key(part, MYDICT)
    ciphertext = clean_text(text, LETTERS)
    for character in ciphertext:
        encrypted_text = MYDICT[character]
        encoded_text = (encrypted_text - key) % 26
        plaintext += LETTERS[encoded_text]
    return plaintext


def choose_encipher_decipher(key, key2, message, cipher_type, encrypt_or_decrypt):
    """ Determines which cipher to run, and whether to encrypt or decrypt.

    Args:
        key:  The key to use for enciphering or deciphering.
        message:  The message to encipher or decipher.
        cipher_type: Type of algorithmn to use.
        encrypt_or_decrypt:  Whether to perform encryption or decryption.
            Encryption = 1, Decrpytion = 2.

    Return:
        The result of either eciphering or deciphering.
    """
    if cipher_type == "shift" and encrypt_or_decrypt == 1 :
        result = shift_cipher(key, message)
        return result
    elif cipher_type == "shift" and encrypt_or_decrypt == 2 :
        result = shift_decipher(key, message)
        return result
    elif cipher_type == "affine" and encrypt_or_decrypt == 1 :




print("\n\nPlease select a Substitution Cipher to use:")

cipher_type = int(input("Monoalphabetic [1]; Polyalphabetic [2]; Affine [3] \n> "))

if cipher_type == 1:
    print("\nMonoalphabetic cipher chosen.\n")
    repeat = True
    while repeat:
        en_or_de = int(input("Encipher [1] or Decipher [2] \n> "))
        key = get_key()
        print("\nKey is " + str(key))
        print("\nPlease enter your message to be encrypted:") if en_or_de == 1 else print("\nPlease enter your message to be decrypted:")
        message = input("> ")
        result = choose_encipher_decipher(key, message, "shift", en_or_de )
        print("\nEncrypted message is: " + result) if en_or_de == 1 else print("\nDecrypted message is: " + result)

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