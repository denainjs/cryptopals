import random
import sys

sys.path.insert(1, '../../set1/challenge7/')
from challenge7 import aes_ecb_encrypt, aes_ecb_decrypt

sys.path.insert(1, '../challenge10/')
from challenge10 import pad, unpad, aes_cbc_encrypt, aes_cbc_decrypt

def encryption_oracle(plaintext, blocksize=16, keysize=16):
    # generate random key
    key = bytes([random.randint(0,255) for i in range(keysize)])

    # append bytes before and after plaintext and add padding
    num_before = random.randint(5,10)
    num_after = random.randint(5,10)
    mod_plaintext = bytes([random.randint(0,255) for _ in range(num_before)]) + plaintext.encode() + bytes([random.randint(0,255) for _ in range(num_after)])
    padded_mod_plaintext = pad(mod_plaintext, blocksize)
    
    # choose encryption method
    method = random.randint(0,1)

    # if encryption method is ECB
    if method == 0: 
        return aes_ecb_encrypt(padded_mod_plaintext, key)
    
    # if encryption method is CBC
    else:
        # choose IV at random
        iv = bytes([random.randint(0,255) for i in range(blocksize)])
        return  aes_cbc_encrypt(padded_mod_plaintext, key, iv)

if __name__ == "__main__":
    plaintext = "asnoetuhsaneouhasnoteuhasnetuhasnoetuhasnteouh"
    e = encryption_oracle(plaintext)
    print(e)