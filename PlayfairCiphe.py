import re

# Function to create the 5x5 matrix for the key
def generate_key_matrix(key):
    matrix = []
    key = key.replace("J", "I")  # Replace J with I for a 5x5 grid
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates while preserving order
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = key + "".join([char for char in alphabet if char not in key])
    
    for i in range(0, 25, 5):
        matrix.append(list(key_matrix[i:i+5]))
        
    return matrix

# Function to locate the position of each character in the key matrix
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

# Function to prepare the text for encryption/decryption
def prepare_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper())
    text = text.replace("J", "I")  # Replace J with I for consistency
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i+1 < len(text) and text[i] == text[i+1]:
            prepared_text += "X"  # Insert 'X' between repeating letters
        elif i+1 < len(text):
            prepared_text += text[i+1]
        i += 2
    if len(prepared_text) % 2 != 0:
        prepared_text += "X"  # Add padding if the length is odd
    return prepared_text

# Function to encrypt/decrypt text using the Playfair cipher
def playfair(text, key, mode='encrypt'):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_text(text)
    result = ""
    
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            if mode == 'encrypt':
                result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == 'encrypt':
                result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    
    return result

# Main function to get user input
def main():
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter text: ").strip().upper()
    key = input("Enter key: ").strip().upper()
    
    if mode == 'encrypt':
        encrypted_text = playfair(text, key, mode='encrypt')
        print("Encrypted Text:", encrypted_text)
    elif mode == 'decrypt':
        decrypted_text = playfair(text, key, mode='decrypt')
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid mode selected. Choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
