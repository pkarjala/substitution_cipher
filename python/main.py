# A nice interface for trying out various ciphers.
# Requires Python 3.x

from cipher import *

def get_key():
    """ Gets a key from the user.

    Key must be of a length of only one character.

    Args:
        none

    Returns:
        The key input by the user.
    """
    print("\nPlease enter your key.")
    key = input("> ")
    # while len(key) > 1:
    #     print("\nKey length is greater than one letter; please", 
    #             "enter a single character key:")
    #     key = input("> ")
    return key

def choose_encipher_decipher(key, message, cipher_type, encrypt_or_decrypt):
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
    if cipher_type == "monoshift" and encrypt_or_decrypt == 1 :
        result = mono_shift_cipher(key, message)
        return result
    elif cipher_type == "monoshift" and encrypt_or_decrypt == 2 :
        result = mono_shift_decipher(key, message)
        return result
    #elif cipher_type == "monoaffine" and encrypt_or_decrypt == 1 :
        #result = 



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
        result = choose_encipher_decipher(key, message, "monoshift", en_or_de )
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
    repeat = True
    while repeat:
        en_or_de = int(input("Encipher [1] or Decipher [2] \n> "))
        repeat = False
else:
    print("\nSorry; a valid choice was not made.\n")