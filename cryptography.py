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
enewnums = []
eend = []
dnumlist = []
dkeynumlist = []
dnewnums = []
dend = []

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
        
        for a in ezip:
            if a[0]+a[1] < len(associations):
                enewnums.append(a[0] + a[1])
            else:
                enewnums.append(a[0] + a[1] - len(associations))
        
        for i in enewnums:
            eend.append(associations[i])
            
        print(''.join(eend))

#+KF;B(CH=NIZ}m;R\Dt

    if edq == "d":

        dmessage = input("Message: ")
        dkey = input("Key: ")
        deekey = dkey
        while len(dkey) < len(dmessage):
            dkey = dkey + deekey
        for x in dmessage:
            dnumlist.append(associations.find(x))
        for y in dkey:
            dkeynumlist.append(associations.find(y))
             
        dzip = list(zip(dnumlist, dkeynumlist))
        
        for a in dzip:
            if a[0]-a[1] > 0:
                dnewnums.append(a[0] - a[1])
            elif a[0]-a[1] <= 0:
                dnewnums.append(a[0] - a[1] + len(associations))
        
        for i in dnewnums:
            dend.append(associations[i])
            
        print(''.join(dend))

    
    if edq != "d" and edq != "e" and edq !="q":
        print("Did not understand command, try again.")
        
    edq = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if edq == "q":
    print("Goodbye!")