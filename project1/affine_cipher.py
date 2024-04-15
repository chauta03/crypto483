# This file contains the implementation of the affine cipher
# The affine cipher is a type of monoalphabetic substitution cipher,
# where each letter in an alphabet is mapped to its numeric equivalent, 
# encrypted using a simple mathematical function, and converted back to a 
# letter.

import string

# This function takes a message and a substitution dictionary and returns 
# the encoded message
#  - message: the message to encode
#  - subst: the substitution dictionary
# return: the encoded message
def encode(message, subst):
  return "".join(subst.get(x, x) for x in message)


# This function creates an affine cipher
#  - a: the first coefficient of the affine cipher
#  - b: the second coefficient of the affine cipher
# return: the encoding and decoding dictionaries
def create_affine_cipher(a, b):
    # create the encoding and decoding dictionaries
    encoding = {}
    decoding = {}

    # size of the alphabet
    alphabet_size = len(string.ascii_uppercase)

    # iterate over the alphabet
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i*a + b) % alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding


# This function compares the message with the encoded message
# the encoded message
#  - message: the message to encode
#  - subst: the substitution dictionary
# print("[PASS]") if the encoded message is the same as the message
# print("[FAIL]") otherwise
def encode_cmp(message, subst):
    # encode the message
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

# test the affine cipher
test_message = "TEST_MESSAGE"
subst, unsubst = create_affine_cipher(10, 2)
if encode_cmp(test_message, subst) == encode(test_message, subst):
    print("[PASS]")
else:
    print("[FAIL]")