import sys

sys.path.insert(1, '../challenge3/')
from challenge3 import decrypt, chi_square


if __name__ == "__main__":
    ref = open("ref.txt", 'r')
    ref_text = ref.read()

    data = open("ciphertext.txt", 'r')
    l = data.readlines()

    n = len(l)
    for i in range(n):
        s = s = l[i][:-1] if (i!=n-1) else l[-1] 
        for key in range(0,256):
            d = decrypt(s, key)
            chi_sq = chi_square(d, ref_text)
            if chi_sq < 10**100: # found it this way, could ask more of chi_sq to narrow down
                print("string index: ", i, "key: ", key, "text: ", d, "chi-square: ", chi_sq)