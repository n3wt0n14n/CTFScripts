#!/usr/bin/python3

import sys,base64

# Decodes JWT cookie data and provides hash for John the Ripper

key = {'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011',
       'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
       'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
       'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
       'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011',
       'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
       'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011',
       'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
       'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
       'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
       'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011',
       's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
       'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011',
       '0': '110100', '1': '110101', '2': '110110', '3': '110111',
       '4': '111000', '5': '111001', '6': '111010', '7': '111011',
       '8': '111100', '9': '111101', '+': '111110', '/': '111111'
}

if len(sys.argv) != 2:
    print("Usage:\t{} [base64 value]".format(sys.argv[0]))
else:
    input = sys.argv[1]

    header, payload, sig = input.split('.')

    # Padding correction
    while len(header)%4 != 0:
        header += "="
    while len(payload)%4 != 0:
        payload += "="
    while len(sig)%4 != 0:
        sig += "="

    print("\nHeader:\t\t{}\nPayload:\t{}\nSignature:\t{}\n".format(base64.standard_b64decode(header).decode('ascii'),base64.standard_b64decode(payload).decode('ascii'),sig))

    conv = ""

    for c in sig:
        if c != "=":
            conv += key[c]

    cnt = 1
    part = ""
    hx   = ""

    for b in conv:
        part += b
        if cnt % 4 == 0:
            hx   += hex(int(part,2))[2:]
            part = ""
        cnt += 1
    print("{}.{}#{}".format(header,payload,hx))
