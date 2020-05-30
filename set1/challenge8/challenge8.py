import binascii
import sys

sys.path.insert(1, '../challenge6/')
from challenge6 import normalized_edit_distance

if __name__ == "__main__":
    ciphertext_hex = open("ciphertext_hex.txt", 'r')
    normalized_edit_distances = []
    lines = ciphertext_hex.readlines()
    for line in lines:
        line_bin = binascii.a2b_hex(line[:-1].encode())
        normalized_edit_distances.append(normalized_edit_distance(16, line_bin))
    # we notice that there is one particular line for which the distance is much smaller than the others
    idx = normalized_edit_distances.index(min(normalized_edit_distances))
    print("encrypted line index: ", idx)
    print("encrypted line hex: ", lines[idx])