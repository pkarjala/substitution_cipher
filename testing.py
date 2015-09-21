# Intended for writing tests
# Requires Python 3.x
# You can easily write any test functions here, especially for trying to brute
# force attack against certain encrypted texts.

from cipher import *

coprime = [1,3,5,7,9,11,15,17,19,21,23,25]
for test in range(26):
    for prime in coprime:
        print( "<", prime, ",", test, "> : ", mono_affine_decipher([prime, test], "uwdqdlfvenvrfxiduqjuw") )