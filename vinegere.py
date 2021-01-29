#!/usr/bin/python3

import sys

def help():
    print("Usage:")
    print("   $ {} -d [ciphertext] [key]".format(sys.argv[0]))
    print("   $ {} -e [plaintext] [key]".format(sys.argv[0]))
    exit()

if len(sys.argv) != 4:
    help()
else:
    key = sys.argv[3]
    ct  = sys.argv[2]
    cnt = 0
    pt  = ''

    # Decoding
    if   sys.argv[1] == '-d':
        de = -1
    elif sys.argv[1] == '-e':
        de = 1
    else:
        print("Invalid encoding/decoding arugment: '{}'".format(sys.argv[1]))
        help()

    for c in ct:
        k = key[cnt%len(key)]
        if   ord(k) >= ord('A') and ord(k) <= ord('Z'):
            shift = ord(k) + (de*ord('A'))
        elif ord(k) >= ord('a') and ord(k) <= ord('z'):
            shift = ord(k) + (de*ord('a'))
        else:
            print("Invalid Key Character: {}".format(k))
            help()
        # Check if upper case, lower case, or not a letter
        if   ord(c) >= ord('A') and ord(c) <= ord('Z'):
            # Upper case
            pt += chr((ord(c) - (de*ord('A')) - shift) % 26 + ord('A'))
            cnt += 1
        elif ord(c) >= ord('a') and ord(c) <= ord('z'):
            # Lower case
            pt += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            cnt += 1
        else:
            # Not a character
            pt += c

    if sys.argv[1] == '-d':
        print("Ciphertext: {}".format(ct))
        print("Key:        {}".format(key))
        print("Plaintext:  {}".format(pt))
    elif sys.argv[1] == '-e':
        print("Plaintext:  {}".format(ct))
        print("Key:        {}".format(key))
        print("Ciphertext: {}".format(pt))
