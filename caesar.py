#!/usr/bin/python3

import sys

def help():
    print("Usage:")
    print("   $ {} [rot13 string]                 # Decodes standard ROT13 ciphertext".format(sys.argv[0]))
    print("   $ {} -n [key] [cipher]              # Decodes Caesar ciphertext with known key".format(sys.argv[0]))
    print("   $ {} -a [unknown ceasar cipher]     # Decodes Caesar ciphertext will all possible keys".format(sys.argv[0]))

def caesar(cipher, shift):
    pt = ""
    for letter in cipher:
        n = ord(letter)

        # Upper Case Letters
        if n >= ord('A') and n <= ord('Z'):
            x = ((n-ord('A')) + shift)%26 + ord('A')
            pt += chr(x)
        # Lower Case Letters
        elif n >= ord('a') and n <= ord('z'):
            x = ((n-ord('a')) + shift)%26 + ord('a')
            pt += chr(x)
        # Not a letter
        else:
            pt += letter
    return pt

if len(sys.argv) < 2 or len(sys.argv) > 4:
    help()
else:
    # Known Caesar Cipher Key or ROT13
    if sys.argv[1] == '-n' or len(sys.argv) == 2:
        # Known Caesar Cipher
        if sys.argv[1] == '-n':
            if len(sys.argv) != 4:
                help()
                exit()
            else:
                shift  = int(sys.argv[2])
                cipher = sys.argv[3]
        else:
            shift  = 13
            cipher = sys.argv[1]
        print("Ciphertext: {}".format(cipher))
        print("Plaintext:  {}".format(caesar(cipher,shift)))
    # Known Caesar Cipher, prints out all possible possibilities
    elif sys.argv[1] == '-a':
        if len(sys.argv) != 3:
            help()
        else:
            cipher = sys.argv[2]
            for i in range(0,26):
                print("{}\t{}".format(i,caesar(cipher,i)))
