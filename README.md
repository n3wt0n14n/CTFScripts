# Useful CTF Scripts and Information
These are a handful of scripts I've seen commonly used in various CTF competitions but frequently forgot how to properly use them.

## caesar.py
Python script that will run through various uses of a Caesar Cipher. With only a ciphertext supplied, the script will decode the ciphertext as ROT13.

Using the `-n` with a `key` integer will decodes the ciphertext with the supplied key.

Using the `-a` tag will run through all possible variations of a Caesar Cipher.

```
Usage:
   $ ./caesar.py [rot13 string]                 # Decodes standard ROT13 ciphertext
   $ ./caesar.py -n [key] [cipher]              # Decodes Caesar ciphertext with known key
   $ ./caesar.py -a [unknown ceasar cipher]     # Decodes Caesar ciphertext will all possible keys
```

## convert.py
Python script that can convert between various number formats.

```
Usage:	./convert.py -[input tag] [value] -[output tag]

 Format Tags:
	-2,  --bin         Binary
	-8,  --oct         Octal
	-10, --dec         Decimal
	-16, --hex         Hexadecimal
	-64, --b64         Base64

 Example: 
   $ ./convert.py -bin 1010 -dec
     10

```

## jwt2john.py
Python script that takes a **JSON Web Token** `JWT` and converts it to a format suitable for John the Ripper (as of v1.9.0-jumbo-1+bleeding-a624a040a from Github source).

```
Usage:	./jwt2john.py [base64 value]
```

## RSA_Basics.md
Markdown file with basic RSA encryption equations and examples to help build your own scripts.

## vinegere.py
Python script to encoding or decoding Vinegere ciphers with a supplied key.

```
Usage:
   $ ./vinegere.py -d [ciphertext] [key]
   $ ./vinegere.py -e [plaintext] [key]

```
