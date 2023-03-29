
#Your program should get the “key size” from the user in terms of number of bits (for instance, 
#64, 128, etc). Based on the size, use Fermat or Miller-Rabin primality test algorithm to define 
#your large prime number. You can use the existing programming packages to find a generator 
#of your finite field. Your program should then initialize a pair of key, i.e., private and public keys. 
#For the computations, utilize the Square-and Multiply algorithm. In fact, your program should 
#get a plaintext from the user to perform encryption (generating the ciphertext from the plaintext) 
#and decryption (generating the original plaintext from the ciphertext).

import random
import math

# Function to perform a single iteration of the Miller-Rabin primality test
def miller_rabin_test(n, k):
    # Check for base cases that are not prime
    if n <= 1 or n % 2 == 0:
        return False
    # Check for small primes
    if n == 2 or n == 3:
        return True

    # Compute r and d such that n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations of the Miller-Rabin test
    for _ in range(k):
        # Choose a random witness a in the range [2, n-2]
        a = random.randrange(2, n - 1)
        # Compute x = a^d mod n
        x = square_and_multiply(a, d, n)

        # If x == 1 or x == n-1, continue to next iteration
        if x == 1 or x == n - 1:
            continue

        # Repeat r-1 times
        for _ in range(r - 1):
            # Compute x = x^2 mod n
            x = square_and_multiply(x, 2, n)
            # If x == n-1, continue to next iteration
            if x == n - 1:
                break
        # If x is not equal to n-1, then n is composite
        else:
            return False

    # If the test passes for all iterations, n is probably prime
    return True

# Function to check if a number is prime using the Miller-Rabin primality test
def is_prime(n, k=5):
    return miller_rabin_test(n, k)

# Function to generate a random prime number of a specified number of bits
def find_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

# Function to find a primitive root of a prime number using brute force search
def find_primitive_root(p):
    for g in range(2, p):
        # Check if g is a primitive root by checking if g^((p-1)/f) mod p is not equal to 1 for all prime factors f of p-1
        if all(square_and_multiply(g, (p - 1) // f, p) != 1 for f in (2, (p - 1) // 2)):
            return g

# Function to perform modular exponentiation using the square-and-multiply algorithm
def square_and_multiply(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

# Function to generate an ElGamal key pair
def generate_key_pair(bits):
    # Generate a random prime number p and a primitive root g of p
    p = find_prime(bits)
    g = find_primitive_root(p)
    # Choose a random secret exponent x in the range [1, p-2]
    x = random.randint(1, p - 2)
    # Compute the public key h = g^x mod p
    h = square_and_multiply(g, x, p)
    # Return the public key (p, g, h) and the private key x
    return (p, g, h), x

# Function to encrypt a single chunk of the message
def encrypt_chunk(public_key, m):
    # Extract the public key parameters p, g, and h
    p, g, h = public_key
    # Choose a random exponent y in the range [1, p-2]
    y = random.randint(1, p - 2)
    # Compute the ciphertext components c1 = g^y mod p and c2 = m * h^y mod p
    c1 = square_and_multiply(g, y, p)
    c2 = (m * square_and_multiply(h, y, p)) % p
    # Return the ciphertext (c1, c2)
    return c1, c2

# Function to decrypt a single chunk of the message
def decrypt_chunk(private_key, ciphertext):
    # Extract the private key parameters p and x
    p, x = private_key
    # Extract the ciphertext components c1 and c2
    c1, c2 = ciphertext
    # Compute the shared secret s = c1^x mod p
    s = square_and_multiply(c1, x, p)
    # Compute the plaintext message m = c2 * h^-x mod p, where h = g^x mod p is the public key component
    m = (c2 * square_and_multiply(s, p - 2, p)) % p
    # Convert the plaintext message from bytes to a string and return it
    return m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()

# Function to encrypt a message using ElGamal encryption
def encrypt(public_key, plaintext):
    # Extract the public key parameters p, g, and h
    p, _, _ = public_key
    # Break the plaintext message into chunks of length roughly p.bit_length() // 16
    message_chunks = [plaintext[i:i + p.bit_length() // 16] for i in range(0, len(plaintext), p.bit_length() // 16)]
    # Encrypt each chunk using the encrypt_chunk function
    ciphertexts = [encrypt_chunk(public_key, int.from_bytes(chunk.encode(), byteorder='big')) for chunk in message_chunks]
    # Return the list of ciphertexts
    return ciphertexts

# Function to decrypt a message using ElGamal encryption
def decrypt(private_key, ciphertexts):
    # Decrypt each chunk using the decrypt_chunk function and join the resulting strings
    return ''.join([decrypt_chunk(private_key, ciphertext) for ciphertext in ciphertexts])

# Main function to run the ElGamal encryption and decryption process
def main():
    print("El Gamal Implementation by Jose Jaramillo & Marco Rojas\n")

    # Get the desired key size from the user
    bits = int(input("Enter the bit size for the ElGamal key (64, 128, etc...): "))
    # Generate the public and private keys
    public_key, private_key = generate_key_pair(bits)
    # Set the private key to be the public key components plus the secret exponent x
    private_key = public_key[0], private_key
    # Get the plaintext message from the user
    plaintext = input("Enter the plaintext message to encrypt: ")
    # Encrypt the plaintext message using the public key
    ciphertexts = encrypt(public_key, plaintext)
    # Print the encrypted message
    print("\nEncrypted message: ", ciphertexts)
    # Decrypt the ciphertext using the private key
    decrypted_message = decrypt(private_key, ciphertexts)
    # Print the decrypted message
    print("\nDecrypted message: ", decrypted_message)

# Call the main function if this file is run as a script
if __name__ == "__main__":
    main()
