
###Your program should get the “key size” from the user in terms of number of bits (for instance, 
#64, 128, etc). Based on the size, use Fermat or Miller-Rabin primality test algorithm to define 
#your large prime number. You can use the existing programming packages to find a generator 
#of your finite field. Your program should then initialize a pair of key, i.e., private and public keys. 
#For the computations, utilize the Square-and Multiply algorithm. In fact, your program should 
#get a plaintext from the user to perform encryption (generating the ciphertext from the plaintext) 
#and decryption (generating the original plaintext from the ciphertext).

import math

a = math.random()       # 1 < a < p-1    #random integer a as private key for alice
b = math.random()       # 1 < b < p-1    #random integer as private key for bob
p = ""                  # Is a very large Prime number
g = ""                  # Primitive root of p
e = g ** a % p
m = ""                  #plaintext      must be less than very large prime number p?

def generateLargePrime():
    #Fermat or Miller-Rabin primality test algorithm to define your large prime number
    return

def getKeySize():
    
    return

def generate_public_key(p,g,e):

    #generate public key
    #utilize the Square-and Multiply algorithm
    #e = g ** a % p
    public_key = ""
    return public_key(p,g,e)        #public key is (p , g, e)

def generate_private_key():
    #utilize the Square-and Multiply algorithm
    return

def encryption():
    #utilize the Square-and Multiply algorithm
    #C_1 = g**b % p
    #C_2 = m * e**b % p
    #Cipher text = (C_1, C_2)
    return

def decryption():
    #utilize the Square-and Multiply algorithm
    #Alice uses Private key to decrypt Bob's cipher text
    #x =(C_1)**a % p
    #m = C_2 * x**(p-2) % p
    
    return


def sendPublicKey():
    return

def main():
    #Alice generate private and public key
    #sends public key to Bob
    generateLargePrime()
    getKeySize()
    generate_public_key(p,g,e)
    generate_private_key()
    sendPublicKey()
    encryption()
    decryption()

    return