# Goal: instead of shifting the alphabet, we randomly jumbled the letters

import string
import random

def create_jumbled_cipher():
    encodings = {}
    decoding = {}
    alphabet = list(string.ascii_uppercase)
    jumbled_alphabet = alphabet.copy()
    random.shuffle(jumbled_alphabet)
    for i in range(len(alphabet)):
        encodings[alphabet[i]] = jumbled_alphabet[i]
        decoding[jumbled_alphabet[i]] = alphabet[i]
    return encodings, decoding

def encode(message, subst):
    return "".join(subst.get(x, x) for x in message)
