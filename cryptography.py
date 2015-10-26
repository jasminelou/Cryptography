"""
cryptography.py
Author: Jasmine Lou
Credit: classmates, the internet, Mr. Dennison

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

edq = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if edq == "e":
    emessage = input("Message: ")
    ekey = input("Key: ")
    emessagelist = print(list(emessage))
    ekeylist = print(list(ekey))

if edq == "d":
    dmessage = input("Message: ")
    dkey = input("Key: ")

if edq == "q":
    print("Goodbye!")