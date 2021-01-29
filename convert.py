#!/usr/bin/python3

import sys, codecs, base64

####################################################################
#                                                                  #
#                   Input Converting Functions                     #
#                                                                  #
####################################################################
def from2(i):
    return int(i,2)

def from8(i):
    return int(i,8)

def from10(i):
    return int(i)

def from16(i):
    return int(i,16)

def from64(i):
    return int.from_bytes(base64.b64decode(i),'big')

def fromAscii(text):
    hx   = ""
    for letter in text:
        hx += hex(ord(letter))[2:]
    return from16(hx)

####################################################################
#                                                                  #
#                   Output Converting Functions                    #
#                                                                  #
####################################################################
def to2(y):
    return bin(y)[2:]

def to8(y):
    return oct(y)[2:]

def to10(y):
    return y

def to16(y):
    return hex(y)[2:]

def to64(y):
    return codecs.encode(codecs.decode(hex(y)[2:],'hex'),'base64').decode()

def toAscii(y):
    return bytes.fromhex(to16(y)).decode('ASCII')

def help():
    print("Usage:\t{} -[input tag] [value] -[output tag]".format(sys.argv[0]))
    print("\n Format Tags:")
    print("\t-2,  --bin         Binary")
    print("\t-8,  --oct         Octal")
    print("\t-10, --dec         Decimal")
    print("\t-16, --hex         Hexadecimal")
    print("\t-64, --b64         Base64")
    print("\t-ascii, --ascii    ASCII")
    print("\n Example: \n   $ {} -bin 1010 -dec".format(sys.argv[0]))
    print("     10\n")

if len(sys.argv) != 4:
    help()
else:
    try:
        # Process input variables
        n = sys.argv[1]

        if   n == '-2'  or n == '--bin':
            x = from2(sys.argv[2])
        elif n == '-8'  or n == '--oct':
            x = from8(sys.argv[2])
        elif n == '-10' or n == '--dec':
            x = from10(sys.argv[2])
        elif n == '-16' or n == '--hex':
            x = from16(sys.argv[2])
        elif n == '-64' or n == '--b64':
            x = from64(sys.argv[2])
        elif n == '-ascii' or n == '--ascii':
            x = fromAscii(sys.argv[2])
        else:
            print("Invalid input option\n")
            help()
            exit()

        # Process output variables
        o = sys.argv[3]

        if   o == '-2'   or o == '--bin':
            print(to2(x))
        elif o == '-8'   or o == '--oct':
            print(to8(x))
        elif o == '-10'  or o == '--dec':
            print(to10(x))
        elif o == '-16'  or o == '--hex':
            print(to16(x))
        elif o == '-64'  or o == '--b64':
            print(to64(x))
        elif o == '-ascii' or o == '--ascii':
            print(toAscii(x))
        else:
            print("Invalid output option: {}\n".format(o))
            help()
            exit()

    except ValueError:
        print("Value Error\n")
        help()
        exit()
