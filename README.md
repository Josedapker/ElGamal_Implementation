ElGamal Encryption Algorithm
This Python code implements the ElGamal encryption algorithm for encrypting and decrypting messages.

Requirements
The code requires Python 3.x to be installed on your machine.

Usage
To run the code, simply execute the following command in your terminal:

Copy code
python3 Assignment3.py

The code will prompt you to enter the bit size for the ElGamal key, which determines the size of the prime number used in the encryption. Next, you will be asked to enter the plaintext message that you want to encrypt.

The program will then generate a public and private key pair using the ElGamal algorithm, encrypt the plaintext message using the public key, and output the encrypted message in the form of a list of ciphertexts.

Finally, the program will decrypt the ciphertexts using the private key and output the decrypted message.

Functions
The code contains several functions, each responsible for a specific task:

miller_rabin_test(n, k): Performs the Miller-Rabin primality test on the input integer n with k iterations. 
Returns True if n is likely to be prime, and False otherwise.

is_prime(n, k=5): Wrapper function for miller_rabin_test() that checks whether an input integer n is prime with k iterations. 
Returns True if n is likely to be prime, and False otherwise.

find_prime(bits): Generates a random prime number with bits number of bits using the random module and the is_prime() function.

find_primitive_root(p): Finds a primitive root of the prime number p.

square_and_multiply(base, exponent, modulus): Computes the modular exponentiation of base to the power of exponent modulo modulus.

generate_key_pair(bits): Generates a public and private key pair for the ElGamal encryption algorithm using a prime number with bits number of bits. 
Returns the public and private keys.

encrypt_chunk(public_key, m): Encrypts a single chunk of plaintext m using the ElGamal encryption algorithm and the given public_key. 
Returns the ciphertext as a tuple (c1, c2).

decrypt_chunk(private_key, ciphertext): Decrypts a single chunk of ciphertext using the ElGamal encryption algorithm and the given private_key. 
Returns the plaintext message as a string.

encrypt(public_key, plaintext): Breaks the plaintext message into chunks and encrypts each chunk using the encrypt_chunk() function and the given public_key. 
Returns the ciphertext as a list of tuples.

decrypt(private_key, ciphertexts): Decrypts the ciphertexts using the decrypt_chunk() function and the given private_key. 
Returns the decrypted plaintext message as a string.
