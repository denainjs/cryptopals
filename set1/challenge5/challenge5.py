import sys

sys.path.insert(1, '../challenge1/')
from challenge1 import hex_to_b64, b64_to_text

sys.path.insert(1, '../challenge2/')
from challenge2 import xor

if __name__ == "__main__":
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    k = ''.join(["ICE"[i%3] for i in range(len(s))])

    # test 1: get correct encrypted hex
    s_hex = s.encode().hex()
    k_hex = k.encode().hex()
    c_hex = xor(s_hex, k_hex)
    c_ans = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    print("test 1: encryption: ", c_hex == c_ans)

    # test 2: recover original string by decrypting
    recov_s_hex = xor(c_hex, k_hex)
    recov_s_b64 = hex_to_b64(recov_s_hex)
    recov_s = b64_to_text(recov_s_b64)
    print("test 2: decryption: ", recov_s == s)