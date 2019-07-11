#This module will take the message and encode/decode with the predefined codebook.
import sys
import string
import random
import json

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

    #Make an encryption dictionary with two lists above
    encryptor = dict(zip(orig_list, key_list))

    print('Encryptor', encryptor)

    # #Save the above dictionary(encryptor) to a json file
    enc_json = json.dumps(encryptor)
    f = open("encryptor.json", "w")
    f.write(enc_json)
    f.close()

    #Make a decryption dictionary by reversing the encryptor dictonary
    decryptor = {}
    for k in encryptor:
        x = encryptor[k]
        decryptor[x] = k

    # #Save the above dictionary(encryptor) to a json file
    dec_json = json.dumps(decryptor)
    f = open("decryptor.json", "w")
    f.write(dec_json)
    f.close()

    print('Decryptor:', decryptor)

if __name__ == '__main__':
    initCodeBook()
