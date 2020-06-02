import base64
def pad(plaintext, blocksize):
    remaining_bits = blocksize - len(plaintext) % blocksize
    padding = (remaining_bits * chr(remaining_bits)).encode()
    return(plaintext + padding)

if __name__ == "__main__":
    plaintext = b"YELLOW SUBMARINE"
    blocksize = 20
    padded = pad(plaintext, blocksize)
    print(padded)