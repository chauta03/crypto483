import string

def create_shift_substitutions(n):
    encodings = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(len(alphabet_size)):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n) % alphabet_size]

        encodings[letter] = subst_letter
        decoding[subst_letter] = letter
    return encodings, decoding
