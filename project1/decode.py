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

# brute force any substitution cipher decoder (WILL NOT WORK BECAUSE OF TIME LIMIT)
def brute_force_substitution_decoder(plaintext, cipher):
    BASE = [i for i in range(26)]

    # O(26!)
    perms = list(permutations(BASE)) 

    for perm in perms:
        substi_dict = {}
        for i in range(26):
            substi_dict[string.ascii_uppercase[i]] = perm[i]
        decoded = "".join(substi_dict.get(x, x) for x in cipher)
        if decoded == plaintext:
            return substi_dict
    return None

# Test decoder
def test_decoder():
    # Test the brute force shift cipher decoder
    print("Test the brute force shift cipher decoder")
    plaintext = "HELLO"
    cipher = "LIPPS"
    shift_dict = brute_force_shift_decoder(plaintext, cipher)
    if shift_dict is not None:
        print("[PASS]")
        print("Shift dictionary:", shift_dict)
        print("Decoded message:", "".join(shift_dict.get(x, x) for x in cipher))
    else:
        print("[FAIL]")


test_decoder()