import sys
sys.path.insert(1, '../challenge3/')
from challenge3 import decrypt, chi_square, ref_text


if __name__ == "__main__":
    data = open("data.txt", 'r')
    l = data.readlines()
    n = len(l)
    print(n)
    for i in range(n):
        if i!=n-1:
            s = l[i][:-1] # remove the \n
        else:
            s = l[-1] # last line has no \n
        for key in range(0,256):
            d = decrypt(s, key)
            chi_sq = chi_square(d, ref_text)
            if chi_sq < 10**100: # found it this way, could ask more of chi_sq to narrow down
                print("string index: ", i, "key: ", key, "text: ", d, "chi-square: ", chi_sq)

# answer: Now that the party is jumping