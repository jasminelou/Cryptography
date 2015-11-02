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
enumlist = []
ekeynumlist = []

while edq != "q":
    
    if edq == "e":
        emessage = input("Message: ")
        ekey = input("Key: ")
        eeekey = ekey
        while len(ekey) < len(emessage):
            ekey = ekey + eeekey
        for x in emessage:
            enumlist.append(associations.find(x))
        for y in ekey:
             ekeynumlist.append(associations.find(y))
             
        ezip = list(zip(enumlist, ekeynumlist))
        print(ezip)

    if edq == "d":
        dmessage = input("Message: ")
        dkey = input("Key: ")
        dmessagelist = print(list(dmessage))
        dkeylist = print(list(dkey))
    
    if edq != "d" and edq != "e" and edq !="q":
        print("Did not understand command, try again.")
        
    edq = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if edq == "q":
    print("Goodbye!")