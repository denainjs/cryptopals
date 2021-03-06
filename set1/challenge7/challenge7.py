import base64
from Crypto.Cipher import AES

def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def aes_ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

if __name__ == "__main__":
    # fetch and decode ciphertext    
    ciphertext_file = open("ciphertext_b64.txt", 'r')
    ciphertext_b64 = ciphertext_file.read()
    ciphertext = base64.b64decode(ciphertext_b64)
    # define cipher
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    # obtain plaintext
    plaintext = aes_ecb_decrypt(ciphertext, key)
    print(plaintext.decode())
