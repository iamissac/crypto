#This module will take the message and encode/decode with the predefined codebook.

import sys
import string
import random

def encrypt(plaintext):

    print("encrypted")

    encrypted_text = plaintext [::-1]

    return encrypted_text

def inputCode():

    plaintext = input("Please enter the plaintext to encrypt: ")

    encrypted_text = encrypt(plaintext)

    print("Thank you, the encrypted will be", encrypted_text)

if __name__ == '__main__':
    inputCode()
