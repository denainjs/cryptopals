import random
import sys

sys.path.insert(1, '../../set1/challenge7/')
from challenge7 import aes_ecb_encrypt, aes_ecb_decrypt

sys.path.insert(1, '../challenge10/')
from challenge10 import pad, unpad, aes_cbc_encrypt, aes_cbc_decrypt

def random_aes_key(keysize=16):
    """generate a random key of size keysize for AES encryption
    """
    return bytes([random.randint(0,255) for i in range(keysize)])

def encryption_oracle(plaintext, blocksize=16, keysize=16):
    """adds characters to plaintext, adds padding, then encrypts with AES
    choose mode at random: ECB with probability 0.5, CBC with probability 0.5
    for both ECB and CBC use a randomly generated 16 bit key
    for CBC use a randomly generated IV

    Returns:
        ciphertext: of type bytes
        mode: "ECB" or "CBC"
    """
    # generate random key
    key = random_aes_key(keysize)

    # append bytes before and after plaintext and add padding
    num_before = random.randint(5,10)
    num_after = random.randint(5,10)
    mod_plaintext = bytes([random.randint(0,255) for _ in range(num_before)]) + plaintext + bytes([random.randint(0,255) for _ in range(num_after)])
    padded_mod_plaintext = pad(mod_plaintext, blocksize)
    
    # choose encryption method
    method = random.randint(0,1)

    # if encryption method is ECB
    if method == 0: 
        return "ECB", aes_ecb_encrypt(padded_mod_plaintext, key)
    
    # if encryption method is CBC
    else:
        # choose IV at random
        iv = bytes([random.randint(0,255) for i in range(blocksize)])
        return  "CBC", aes_cbc_encrypt(padded_mod_plaintext, key, iv)

def detect_mode(ciphertext, blocksize=16):
    """detect whether the ciphertext was obtained by running AES-ECB or AES-CBC
    rule of thumb: if there are repetitions in the ciphertext, then it was probably obtained with AES-ECB
    ciphertext is of type bytes
    """
    block_seen = []
    num_repeats = 0
    for i in range(0, len(ciphertext), blocksize):
        block = ciphertext[i:i+blocksize]
        if block not in block_seen and ciphertext.count(block) > 2:
            num_repeats += ciphertext.count(block)
            block_seen.append(block)
    if num_repeats > 0:
        return "ECB"
    else:
        return "CBC"



if __name__ == "__main__":
    plaintext = 50 * b"this is a plaintext"
    print("plaintext: ", plaintext)
    mode, ciphertext = encryption_oracle(plaintext)
    print("mode: ", mode) 
    print("ciphertext: ", ciphertext)
    print("inferred mode: ", detect_mode(ciphertext, blocksize=16))
    if detect_mode(ciphertext, blocksize=16) == mode:
        print("success!")
    else:
        print("failure!")