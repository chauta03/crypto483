import string
import random

# Create a jumbled cipher
# return: the encoding and decoding dictionaries
def create_jumbled_cipher():
    encoding = {}
    decoding = {}
    alphabet = list(string.ascii_uppercase)
    jumbled_alphabet = alphabet.copy()
    random.shuffle(jumbled_alphabet)
    for i in range(len(alphabet)):
        encoding[alphabet[i]] = jumbled_alphabet[i]
        decoding[jumbled_alphabet[i]] = alphabet[i]
    return encoding, decoding

# This function takes a message and a substitution dictionary and returns
# the encoded message
def encode(message, subst):
    return "".join(subst.get(x, x) for x in message)

# This function takes a message and a substitution dictionary and returns
# the decoded message
def decode(message, subst):
    return encode(message, subst)

# This function compares the message with the encoded message
# the encoded message
#  - message: the message to encode
#  - subst: the substitution dictionary
# print("[PASS]") if the encoded message is the same as the message
# print("[FAIL]") otherwise
def encode_cmp(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

test_message = "TEST_MESSAGE"
subst, unsubst = create_jumbled_cipher()
if encode_cmp(test_message, subst) == encode(test_message, subst):
    print("[PASS]")
    print("Encode: ", subst, "\n","Decode: ", unsubst)
    print("Raw text:", test_message, "->","Encoded message:", encode(test_message, subst), "->","Decoded message: ", decode(encode(test_message, subst), unsubst))
else:
    print("[FAIL]")