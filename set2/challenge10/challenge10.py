import base64
from Crypto.Cipher import AES

def xor(s1, s2):
    """[summary]

    Arguments:
        s1 {[type]} -- string encoded in binary (ie of type bytes)
        s2 {[type]} -- string encoded in binary (ie of type bytes)
    """
    return bytes(a^b for a,b in zip(s1,s2))

def pad(b, blocksize=16):
    remaining_bits = blocksize - len(b) % blocksize
    padding = (remaining_bits * chr(remaining_bits)).encode()
    return(b + padding)

def unpad(b, blocksize=16):
    pad_size = b[-1]
    padding = b[-pad_size:]
    if padding == bytes(pad_size * [pad_size]):
        return b[:-pad_size]
    else:
        return b


def aes_cbc_encrypt(plaintext, key, iv, blocksize = 16):
    cipher = AES.new(key, AES.MODE_ECB) # ok to use ECB mode since there's only one block
    to_xor = iv
    ciphertext = b""
    
    for i in range(0, len(plaintext), blocksize):
        plaintext_block = pad(plaintext[i:i+blocksize], blocksize)
        xor_plaintext_block = xor(to_xor, plaintext_block)
        ciphertext_block = cipher.encrypt(xor_plaintext_block)
        ciphertext += ciphertext_block
        to_xor = ciphertext_block
    return ciphertext

def aes_cbc_decrypt(ciphertext, key, iv, blocksize = 16):
    cipher = AES.new(key, AES.MODE_ECB) # ok to use ECB mode since there's only one block
    
    to_xor = iv
    plaintext = b""
    
    for i in range(0, len(ciphertext), blocksize):
        ciphertext_block = ciphertext[i:i+blocksize]
        decrypted_block = cipher.decrypt(ciphertext_block)
        plaintext_block = xor(to_xor, decrypted_block)
        plaintext += unpad(plaintext_block, blocksize)
        to_xor = ciphertext_block
    return plaintext

if __name__ == "__main__":
    f = open("ciphertext.txt", 'r')
    ciphertext = base64.b64decode(f.read())
    key = b"YELLOW SUBMARINE"
    blocksize = 16
    iv = blocksize * chr(0).encode()

    print("iv: ", iv)
    print("ciphertext: ", ciphertext)
    plaintext = aes_cbc_decrypt(ciphertext, key, iv)
    print("plaintext: ", plaintext)
    back_to_ciphertext = aes_cbc_encrypt(plaintext, key, iv)
    print("back to ciphertext: ", back_to_ciphertext)
    back_to_plaintext = aes_cbc_decrypt(back_to_ciphertext, key, iv)
    print("and back to plaintext: ", back_to_plaintext)