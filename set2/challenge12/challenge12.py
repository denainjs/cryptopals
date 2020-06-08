import base64
import sys

sys.path.insert(1, '../challenge11/')
from challenge10 import random_aes_key

sys.path.insert(1, '../../set1/challenge7')
from challenge7 import aes_ecb_encrypt

KEY = random_aes_key()
UNKNOWN_STRING =b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\naGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\ndXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\nYnkK"

def encrypt_buffer(plaintext, key=KEY, to_append=UNKNOWN_STRING):
    """append base64 decoded TO_APPEND to plaintext then encrypt with AES-ECB
    key, to_append, plaintext and ciphertext are all bytes objects
    """
    to_append_decode = base64.b64decode(to_append)
    to_encrypt = plaintext + to_append_decode
    ciphertext = aes_ecb_encrypt(to_encrypt, key)
    return ciphertext

# the general idea here is: use ECB with a random key to encrypt UNKNOWN_STRING
# we treat both the key and UNKNOWN_STRING as unknown (we can only see the base64 encoding of UNKNOWN_STRING)
# our goal is to recover UNKNOWN_STRING by attacking AES-ECB

if __name__ == "__main__":
    # discover block size

    # detect ECB

    # 1 byte short input block

    # 