import hashlib

def calculate_sha1_digest(text):
    sha1 = hashlib.sha1()
    
    sha1.update(text.encode('utf-8'))
    
    digest = sha1.hexdigest()
    
    return digest

text = input("Enter the text: ")
digest = calculate_sha1_digest(text)
print(f"The SHA-1 digest of '{text}' is: {digest}")
