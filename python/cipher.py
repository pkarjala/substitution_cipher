# This is an implemention of various ciphers in Python.
# Requires Python 3.x
# It uses Z = 26, or the Roman Alphabet for character input.

# Imports
from math import floor


# Global Constants
LETTERS = "abcdefghijklmnopqrstuvwxyz"
MY_DICT = { LETTERS[i]:i for i in range(len(LETTERS)) }


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

    If the key is already an integer, simply returns the key.

    Args:
        key:  The key to translate.

    Returns:
        The key as an integer.

    """
    if key in mapping:
        key = mapping[key]
    return key


def mono_shift_cipher(key, text):
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
    key = translate_key(key, MY_DICT)
    message = clean_text(text, LETTERS)
    for character in message:
        encoded_text = MY_DICT[character]
        encrypted_text = (encoded_text + key) % 26
        ciphertext += LETTERS[encrypted_text]
    return ciphertext


def mono_shift_decipher(key, text):
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
    key = translate_key(key, MY_DICT)
    ciphertext = clean_text(text, LETTERS)
    for character in ciphertext:
        encrypted_text = MY_DICT[character]
        encoded_text = (encrypted_text - key) % 26
        plaintext += LETTERS[encoded_text]
    return plaintext

#Extended Euclidian Algorithm
def extended_euclidian_algorithm(a,b):
    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while r1 != 0:
        q = floor(r0 / r1)
        temp = r0
        r0 = r1
        r1 = temp - q * r1
        temp = s0
        s0 = s1
        s1 = temp - q * s1
        temp = t0
        t0 = t1
        t1 = temp - q * t1
    d = r0
    return [d,s0,t0]



def mono_affine_cipher(key, text):
    ciphertext = ''
    a = translate_key(key[0], MY_DICT)
    b = translate_key(key[1], MY_DICT)
    message = clean_text(text, LETTERS)
    for character in message:
        encoded_text = MY_DICT[character]
        encrypted_text = (encoded_text * a + b) % 26
        ciphertext += LETTERS[encrypted_text]
    return ciphertext

def mono_affine_decipher(key, text):
    plaintext = ''
    a = translate_key(key[0], MY_DICT)
    b = translate_key(key[1], MY_DICT)
    a1 = extended_euclidian_algorithm(26,a)[2] % 26
    ciphertext = clean_text(text, LETTERS)
    for character in ciphertext:
        encrypted_text = MY_DICT[character]
        encoded_text = ( a1*encrypted_text - a1*b) % 26
        plaintext += LETTERS[encoded_text]
    return plaintext


