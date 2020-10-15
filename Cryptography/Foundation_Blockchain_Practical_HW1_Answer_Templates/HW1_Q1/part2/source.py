#Use this library for calculating hash functions
import hashlib
import string
import random
#Do not change the name of the class
class CollisionFinder:
    def __init__(self):
        pass

    def findCollision(self): #Do not change the name of the function

        # Write your code here

        userpass_hash = []
        userpass = []
        indice = []
        N = 20 ;
        Nmax = 20000;
        for i in range(Nmax):
            userpass.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)))
            newuserpass_hash = hashlib.sha256()
            newuserpass_hash.update(userpass[i].encode())
            newuserpass = newuserpass_hash.hexdigest()
            userpass_hash.append(newuserpass[-6:])
        userpass_hash, userpass = (list(t) for t in zip(*sorted(zip(userpass_hash, userpass))))
        for i in range(Nmax-1):
            if userpass_hash[i]==userpass_hash[i+1] :
                indice.append(i)
        print(userpass[indice[0]])
        print(userpass[indice[0]+1])
        print(userpass[indice[1]])
        print(userpass[indice[1]+1])

        # return an array with two strings
        return [userpass[indice[0]], userpass[indice[0]+1],userpass[indice[1]],serpass[indice[1]+1]]
