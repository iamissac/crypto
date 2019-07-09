#This module will take the message and encode/decode with the predefined codebook.

import sys
import string
import random

def initCodeBook():
    #Creates a list of codeBook
    #Original list is alphabet, 26 chars.
    orig_list = []
    orig_list = list(string.ascii_lowercase)
    print('Original List: ', orig_list)

    #Key list is randomly generated punctuation characters, 26.
    key_list = []
    i = 0
    while (i < len(orig_list)):
        key_list.append(random.choice(string.punctuation))
        i += 1

    print('Key List: ', key_list)

    encryptor = dict(zip(orig_list, key_list))

    print('Encryptor', encryptor)

    decryptor = {}

    for k in encryptor:
        x = encryptor[k]
        decryptor[x] = k


    print('Decryptor:', decryptor)

if __name__ == '__main__':
    plaintext = 'hackers for charity'
    initCodeBook()
