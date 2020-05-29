import base64
from Crypto.Cipher import AES

if __name__ == "__main__":
    # fetch and decode ciphertext    
    ciphertext_file = open("ciphertext_b64.txt", 'r')
    ciphertext_b64 = ciphertext_file.read()
    ciphertext = base64.b64decode(ciphertext_b64)
    # define cipher
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    # obtain plaintext
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext.decode())
