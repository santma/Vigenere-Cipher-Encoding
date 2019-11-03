#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:11:48 2019

@author: margaretsant
"""

############### Exercise 1 : Vigenere Cipher ###################

def encryption():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = input('enter message:')
    plaintext = list(message)
    key = input('enter Key:')
    K = [int(i) for i in key.split(',')]
    m = len(K)
    
    ###     Encoding
    
    ek = [plaintext[i:i+m] for i in range(0,len(plaintext),m)]
    
    encrypt = []
    for i in ek:
        position = [alphabet.find(letter) for letter in i]
        for i in range(0,len(position)):
          encrypt.append((position[i] + K[i])%26) 
          
    ciphertext = []
    for i in encrypt:
        c = i + 97
        cipher = chr(c)
        ciphertext.append(cipher)
        
    encrypted_message = ''.join(str(e) for e in ciphertext)
    
    print("message encrypted: ")
    print(encrypted_message)
    return encrypted_message

encryption()

def decryption():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = input('enter coded message:')
    plaintext = list(message)
    key = input('enter Key:')
    K = [int(i) for i in key.split(',')]
    m = len(K)
    
    ###     Encoding
    
    ek = [plaintext[i:i+m] for i in range(0,len(plaintext),m)]
    
    encrypt = []
    for i in ek:
        position = [alphabet.find(letter) for letter in i]
        for i in range(0,len(position)):
          encrypt.append((position[i] - K[i])%26) 
          
    ciphertext = []
    for i in encrypt:
        c = i + 97
        cipher = chr(c)
        ciphertext.append(cipher)
        
    encrypted_message = ''.join(str(e) for e in ciphertext)
    
    print("message encrypted: ")
    print(encrypted_message)

decryption()


############### Exercise 2: ###################

######## A: Index of Coincidence:
string = input('enter string:')
def index_of_coincidence(string):
    n = len(string)
    freq = {i : string.count(i) for i in set(string)}
    values = [(i - 1) for i in freq.values()]
    s = sum(values)
    ic = s / ((n * (n-1))/26)
    print(ic)
index_of_coincidence(string)

######## B: IC Applied to Vigenere Cipher to find m (length of key):


message = input('enter string:')
st = list(message)
m = 4
indexes = []
test = [st[i:i+m] for i in range(0,len(st),m)]
for t in test:
    
    f = index_of_coincidence(t)
    print(f)
















