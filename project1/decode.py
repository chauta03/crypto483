import string

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
