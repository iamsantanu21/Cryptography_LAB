import hashlib

def md5_hash(string):
    md5 = hashlib.md5()
    
    md5.update(string.encode('utf-8'))

    return md5.hexdigest()

input_data = input("Enter the text: ")
hash_result = md5_hash(input_data)
print(f"MD5 Hash of '{input_data}': {hash_result}")
