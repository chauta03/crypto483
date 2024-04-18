import string
from itertools import permutations 

# brute force shift cipher decoder
def brute_force_shift_decoder(plaintext, cipher):
    for i in range(26):
        shift = i
        shift_dict = {}
        for j in range(26):
            shift_dict[string.ascii_uppercase[j]] = string.ascii_uppercase[(j + shift) % 26]
        decoded = "".join(shift_dict.get(x, x) for x in cipher)
        if decoded == plaintext:
            return shift_dict
    return None

# brute force any substitution cipher decoder
def brute_force_substitution_decoder(plaintext, cipher):
    BASE = [i for i in range(26)]
    perms = permutations(BASE)
    perms.remove(BASE)

    for perm in perms:
        substi_dict = {}
        for i in range(26):
            substi_dict[string.ascii_uppercase[i]] = i
        decoded = "".join(substi_dict.get(x, x) for x in cipher)
        if decoded == plaintext:
            return substi_dict
    return None

