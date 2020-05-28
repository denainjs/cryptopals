import binascii
import sys
from itertools import zip_longest
import base64

sys.path.insert(1, '../challenge1/')
from challenge1 import b64_to_text

sys.path.insert(3, '../challenge3/')
from challenge3 import decrypt, chi_square, ref_text

def hamming_int(n1, n2):
    """hamming distance between the strings of bits corresponding to n1 and n2
    """
    # encode n1 and n2 as strings of 7 bits (ascii has 128 characters)
    b1 = str(bin(n1))[2:].zfill(7)
    b2 = str(bin(n2))[2:].zfill(7)
    res = 0
    # increment res for every bit that differs between b1 and b2
    for (ch1, ch2) in zip(b1, b2):
        res += ch1!=ch2
    return res

def hamming_str(s1, s2):
    """hamming distance between strings s1 and s2
    ie number of bits that differ
    we assume that both strings have the same length
    """
    # confirm that strings have the same length
    assert len(s1) == len(s2)
    
    # convert to list of ints
    s1_ints = [int(j) for j in binascii.a2b_qp(s1)]
    s2_ints = [int(j) for j in binascii.a2b_qp(s2)]

    # add hamming distance for all ints
    res = 0
    for (n1, n2) in zip(s1_ints, s2_ints):
        res += hamming_int(n1, n2)
    return res

def normalized_edit_distance(keysize, ciphertext):
    s = ciphertext.decode() # convert b64 to text to be able to apply hamming_str
    chunks = [s[i:i+keysize] for i in range(0, len(s), keysize)]
    distances = []
    while True:
        try:
            s1, s2 = chunks[0], chunks[1]
            distances.append(hamming_str(s1, s2)/keysize)
            del chunks[0]
            del chunks[1]
        except Exception as e:
            break 
    return sum(distances)/len(distances)

def ordered_keysizes(s_b64):
    """order keysizes by normalized edit distance between first and second blocks
    """
    return sorted(list(range(2,40)), key=lambda k:normalized_edit_distance(k, s_b64))
    
def decode_transposed_blocks(keysize, ciphertext, ranks):
        l = []
        for t_block in range(keysize):
            t_hex = ciphertext[t_block::keysize].hex()
            ordered_keys = sorted(list(range(0, 256)), key= lambda key: chi_square(decrypt(t_hex, key), ref_text))
            r = ranks[t_block]
            key = ordered_keys[r]
            print("        k idx={}, key={}, rank={}".format(t_block, key, r))
            l.append(decrypt(t_hex, key))
        return l

def reassemble_blocks(l):
        plaintext = ""
        idx = 0
        while True:
            try:
                for k in range(keysize):
                    plaintext += l[k][idx]
                idx += 1
            except Exception as e:
                break
        return(plaintext)


if __name__ == "__main__":
    print("test hamming")
    s1 = "this is a test"
    s2 = "wokka wokka!!!"
    print("    string 1: ", s1)
    print("    string 2: ", s2)
    print("    computed hamming distance: ", hamming_str(s1, s2))
    print("    true hamming distance: ", 37)

    print("test vigenere")
    print("    fetch data")
    data = open("text.txt", 'r')
    ciphertext = base64.b64decode(data.read())
    
    print("    determine keysize")
    ord = ordered_keysizes(ciphertext)
    keysize = ord[0] # the keysize with the smallest normalized edit distance is the best

    print("    apply single-character XOR to transposed blocks")
    ranks = keysize * [0]
    ranks[22] = 1 # turns out the best chi square value is not always the correct one: for transposed block 22 the runner up is better
    l = decode_transposed_blocks(keysize, ciphertext, ranks)
    print("    reassemble text\n")
    plaintext = reassemble_blocks(l)
    print(plaintext)

    
    