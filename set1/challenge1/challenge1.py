import binascii
import base64

def hex_to_b64(s_hex):
    s_bin = binascii.unhexlify(s_hex) # from hex string to bytes object
    s_b64 = ''.join(chr(x) for x in binascii.b2a_base64(s_bin)[:-1]) # last character is a \n hence [:-1]
    return(s_b64)

def b64_to_text(s_b64):
    s_text = base64.b64decode(s_b64).decode() # first decode: base64 to characters, second decode bytes to string
    return s_text


if __name__ == "__main__":
    print("test 1:")
    s = "hello this is a string"
    print("    original text: ", s)
    s_hex = s.encode().hex() # encode(): from str to bytes object, hex() returns the hex string corresponding to bytes
    print("    hex encoding: ", s_hex)
    s_b64 = hex_to_b64(s_hex)
    print("    base 64 encoding: ", s_b64)
    text = base64.b64decode(s_b64).decode()
    print("    recovered text: ", text)

    print("test 2:")
    s_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print("    hex: ", s_hex)
    s_b64 = hex_to_b64(s_hex)
    print("    base64: ", s_b64)
    text = base64.b64decode(s_b64).decode()
    print("    recovered text: ", text)