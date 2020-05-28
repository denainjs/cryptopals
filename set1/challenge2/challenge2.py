import binascii

def xor(hex1, hex2):
    bin1 = binascii.unhexlify(hex1)
    bin2 = binascii.unhexlify(hex2)
    bin_res = bytes(x^y for x,y in zip(bin1, bin2))
    hex_res = binascii.hexlify(bin_res).decode()
    return(hex_res)

if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    print("hex1 : ", hex1)
    hex2 = "686974207468652062756c6c277320657965"
    print("hex2 : ", hex2)
    print("computed xor: ", xor(hex1, hex2))
    print("actual xor: 746865206b696420646f6e277420706c6179")
    print(xor(hex1, hex2) == "746865206b696420646f6e277420706c6179")

    
