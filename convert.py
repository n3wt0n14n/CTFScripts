#!/usr/bin/python3

import sys, codecs

# Base64 Dictionary
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

####################################################################
#                                                                  #
#                   Input Converting Functions                     #
#                                                                  #
####################################################################
def from2():
    return int(sys.argv[2],2)

def from8():
    return int(sys.argv[2],8)

def from10():
    return int(sys.argv[2])

def from16():
    return int(sys.argv[2],16)

def from64():
    input = sys.argv[2]
    orig  = input

    # Padding correction
    while len(input)%4 != 0:
        input += "="

    if input != orig:
        print("Padding correction:")
        print("   Original:\t{}".format(orig))
        print("   Corrected:\t{}\n".format(input))

    # Initialize the raw conversion array of binary chunks
    conv = ""

    # Constructs the raw conversion array with a binary chunk fur each Base64 character
    for c in input:
        if c != "=":
            conv += key[c]

    # Initializing variables to convert to HEX bytes
    cnt = 1
    part = ""
    hx   = ""

    # Constructs the raw HEX bitstream
    for b in conv:
        part += b
        if cnt % 4 == 0:
            hx   += hex(int(part,2))[2:]
            part = ""
        cnt += 1

    # Converts and returns integer value
    return int(hx,16)

####################################################################
#                                                                  #
#                   Output Converting Functions                    #
#                                                                  #
####################################################################
def to2(y):
    print(bin(y)[2:])

def to8(y):
    print(oct(y)[2:])

def to10(y):
    print(y)

def to16(y):
    print(hex(y)[2:])

def to64(y):
    print(codecs.encode(codecs.decode(hex(y)[2:],'hex'),'base64').decode())

def help():
    print("Usage:\t{} -[input tag] [value] -[output tag]".format(sys.argv[0]))
    print("\n Format Tags:")
    print("\t-2,  --bin         Binary")
    print("\t-8,  --oct         Octal")
    print("\t-10, --dec         Decimal")
    print("\t-16, --hex         Hexadecimal")
    print("\t-64, --b64         Base64")
    print("\n Example: \n   $ {} -bin 1010 -dec".format(sys.argv[0]))
    print("     10\n")

if len(sys.argv) != 4:
    help()
else:
    try:
        # Process input variables
        n = sys.argv[1]

        if   n == '-2'  or n == '--bin':
            x = from2()
        elif n == '-8'  or n == '--oct':
            x = from8()
        elif n == '-10' or n == '--dec':
            x = from10()
        elif n == '-16' or n == '--hex':
            x = from16()
        elif n == '-64' or n == '--b64':
            x = from64()
        elif n == '-13' or n == '--rot':
            x = from13()
        else:
            print("Invalid input option\n")
            help()
            exit()

        #print("x = {}".format(x))

        # Process output variables
        o = sys.argv[3]

        if   o == '-2'   or o == '--bin':
            to2(x)
        elif o == '-8'   or o == '--oct':
            to8(x)
        elif o == '-10'  or o == '--dec':
            to10(x)
        elif o == '-16'  or o == '--hex':
            to16(x)
        elif o == '-64'  or o == '--b64':
            to64(x)
        elif o == '-13'  or o == '--rot':
            to13(x)
        else:
            print("Invalid output option\n")
            help()
            exit()

    except ValueError:
        print("Value Error\n")
        help()
        exit()
