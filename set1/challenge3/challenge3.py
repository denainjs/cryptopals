import base64
import math
import binascii
import string      # definitions of ascii printable chars
from collections import defaultdict     # fast counting
import sys 

sys.path.insert(1, '../challenge1/')
from challenge1 import hex_to_b64

# 'a single character' means a single byte, ie a number between 1 and 256 (to which you can apply ^)

ref = open("ref.txt", 'r')
ref_text = ref.read()

def char_freq(ref_text):
    """character frequencies in a text of reference
    see https://opendata.stackexchange.com/questions/7042/ascii-character-frequency-analysis

    Arguments:
        ref_text {string} -- some text of reference

    Returns:
        a defaultdict containing the 
    """

    d = defaultdict(int)    # define dictionary for counting frequencies

    for ch in ref_text:       # loop over each character 
        if ch in string.printable:     # is the character in the ascii/printable set?
            d[ch] += 1    #   if so, add 1 to that characters frequency counter
    for ch in ref_text:
        d[ch]/len(ref_text)
    return d     # return all frequencies


def decrypt(s_hex, key):
    s_bin = binascii.unhexlify(s_hex)
    d_bin = bytes(x^key for x in s_bin)
    d_hex = binascii.hexlify(d_bin).decode()
    d_b64 = hex_to_b64(d_hex)
    text = base64.b64decode(d_b64).decode(encoding='utf-8',errors="ignore") # if there is an error, we know that the key is not the one we want
    return text

def chi_square(s, ref_text):
    if len(s) == 0:
        return 10**100
    ref_freq = char_freq(ref_text)
    s_freq = char_freq(s)
    T = 0.
    if s_freq == defaultdict(int):
        return 10**100
    else:
        for ch in s_freq:
            if ref_freq[ch] == 0:
                return 10**100
            else:
                T += (len(s) * (ref_freq[ch] - s_freq[ch]))**2 / (len(s) * ref_freq[ch])
        return T

if __name__ == "__main__":
    s_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    for key in range(0,256):
        d = decrypt(s_hex, key)
        chi_sq = chi_square(d, ref_text)
        if chi_sq != 10**100:
            print(d)
    pass

# answer: Cooking MC's like a pound of bacon