import binascii
import base64

if __name__ == "__main__":
    s_hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print("hex (type str): ", s_hex_str)
    s_bin_bytes = binascii.unhexlify(s_hex_str)
    print("binary (type bytes): ", s_bin_bytes)
    s_b64_bytes = binascii.b2a_base64(s_bin_bytes)
    print("base64 (type bytes): ", s_b64_bytes)
    s_b64_str = s_b64_bytes.decode()
    print("base64 (type str): ", s_b64_str)