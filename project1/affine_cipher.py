import string
def encode(message, subst):
  return "".join(subst.get(x, x) for x in message)

def create_affine_cipher(a, b):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i*a + b) % alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding

def encode_cmp(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

test_message = "TEST_MESSAGE"
subst, unsubst = create_affine_cipher(10, 2)
if encode_cmp(test_message, subst) == encode(test_message, subst):
    print("[PASS]")
else:
    print("[FAIL]")