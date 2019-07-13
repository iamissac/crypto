#This module will take the message and encode/decode with the predefined codebook.

import sys
import string
import random
import json



def encrypt(plaintext):

    #print("encrypted")

    with open("encryptor.json", "r") as read_file:
        data = json.load(read_file)

    #print(data)

    for c in plaintext:
        if c in data:
            plaintext = plaintext.replace(c, data[c])

    return plaintext

def decrypt(encrypted_text):

    with open("decryptor.json", "r") as read_file:
        data = json.load(read_file)

    print(data)

    for c in encrypted_text:
        if c in data:
            encrypted_text = encrypted_text.replace(c, data[c])

    return encrypted_text

def inputCode():

    plaintext = input("Please enter the plaintext to encrypt: ")

    encrypted_text = encrypt(plaintext)

    print("Thank you, the encrypted text will be", encrypted_text)

    decrypted_text = decrypt(encrypted_text)
    print("Thank you, the decrypted text will be", decrypted_text)


if __name__ == '__main__':
    inputCode()
