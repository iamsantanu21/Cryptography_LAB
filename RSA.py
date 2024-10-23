import random
from sympy import mod_inverse, isprime

def generate_large_prime():
    while True:
        num = random.randint(2, 100)
        if isprime(num):
            return num

def generate_keypair():
    # Step 1: Choose two prime numbers
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()
    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute phi(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)

    # Step 4: Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randint(2, phi - 1)
    while not (isprime(e) and e < phi):
        e = random.randint(2, phi - 1)

    # Step 5: Compute d, the modular inverse of e mod phi(n)
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(plaintext, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_message

def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

# Example usage:
public_key, private_key = generate_keypair()
print("Public Key:", public_key)
print("Private Key:", private_key)

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    
    choice = int(input("Choose an option (1-3): "))
    
    if choice == 1:
        plaintext = input("Enter the text to encrypt: ")
        encrypted_msg = encrypt(plaintext, public_key)
        print("Encrypted Message:", encrypted_msg)
    
    elif choice == 2:
        ciphertext_input = input("Enter the comma-separated integers to decrypt: ")
        ciphertext_input = ciphertext_input.strip('[]')  # Remove any brackets
        ciphertext = list(map(int, ciphertext_input.split(',')))  # Convert input to list of integers
        decrypted_msg = decrypt(ciphertext, private_key)
        print("Decrypted Message:", decrypted_msg)
    
    elif choice == 3:
        exit()
    
    else:
        print("Invalid option, please try again.")
