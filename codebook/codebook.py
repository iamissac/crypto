#This module will take the message and encode/decode with the predefined codebook.

import sys
import string
import random

def codeBook():
    #It replaces the character
    orig_list = []
    orig_list = list(string.ascii_lowercase)
    keys = []

    #while (len(string.ascii_lowercase)):
    #while (range(0,25)):
    i = 0
    while (i < len(orig_list)):
        keys.append(random.choice(string.punctuation))
        i += 1

    print('Orig:', orig_list)
    print('Punct:', keys)

    encryptor = dict(zip(orig_list, keys))

    print('Encryptor', encryptor)

    decryptor = {}

    for k in encryptor:
        x = encryptor[k]
        decryptor[x] = k


    print('Decryptor:', decryptor)

    # for v in enc:
    #
    #
    # #print('ENC:',enc)
    #
    # dec = {}
    #
    # for k in enc:
    #     x = enc[k]
    #     dec[x] = k
    #
    # print('ENC:',enc)
    # print('DEC:',dec)

if __name__ == '__main__':
    plaintext = 'hackers for charity'
    codeBook()
