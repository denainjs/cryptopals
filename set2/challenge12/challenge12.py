import base64
import sys

sys.path.insert(1, '../challenge11/')
from challenge11 import random_aes_key, detect_mode

sys.path.insert(1, '../../set1/challenge7')
from challenge7 import aes_ecb_encrypt

sys.path.insert(1, '../challenge10/')
from challenge10 import pad


KEY = random_aes_key()
UNKNOWN_STRING =b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\naGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\ndXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\nYnkK"

def encrypt_buffer(plaintext, key=KEY, to_append=UNKNOWN_STRING):
    """append base64 decoded TO_APPEND to plaintext then encrypt with AES-ECB
    key, to_append, plaintext and ciphertext are all bytes objects
    """
    to_append_decode = base64.b64decode(to_append)
    to_encrypt = pad(plaintext + to_append_decode)
    ciphertext = aes_ecb_encrypt(to_encrypt, key)
    return ciphertext

# the general idea here is: use ECB with a random key to encrypt UNKNOWN_STRING
# we treat both the key and UNKNOWN_STRING as unknown (we can only see the base64 encoding of UNKNOWN_STRING)
# our goal is to recover UNKNOWN_STRING by attacking AES-ECB

if __name__ == "__main__":
    # discover block size: 
    lengths = [len(encrypt_buffer(i*b"a")) for i in range(50)]
    for i in range(len(lengths)):
        blocksize = lengths[i+1] - lengths[i]
        if blocksize != 0:
            break
    print('blocksize:', blocksize)

    # detect ECB
    mode = detect_mode(encrypt_buffer(50*b"a"), blocksize=blocksize)
    print("mode:", mode)

    # 1 byte short input block
    # encrypt buffer will append UNKNOWN_STRING to the right of this
    # first block of the resulting string to_encrypt = shortened_block + first byte of UNKNOWN_STRING
    shortened_block = (blocksize-1) * b"A"

    # create dictionary of possible first blocks of to_encrypt
    dic = {}
    for i in range(256): # all ascii characters
        fst_block_plain = shortened_block + chr(i).encode()
        fst_block_cipher = encrypt_buffer(fst_block_plain)[0:blocksize]
        dic[fst_block_cipher] = i
    
    # actual first ciphertext block for shortened_block
    fst_block_cipher = encrypt_buffer(shortened_block)[0:blocksize]
    print("first byte:", dic[fst_block_cipher])
    print("corresponding character:", chr(dic[fst_block_cipher]))