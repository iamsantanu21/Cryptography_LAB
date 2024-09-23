def main(): 
    while True:
        print("\nRailFenceCipher")
        print("1: Encrypt")
        print("2: Decrypt")
        print("3: Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            Text = input("Enter the text to encrypt: ")
            key = int(input("Enter the key (number of rails): "))
            cipherText = cipher(Text, key)
            print("Ciphered Text: "+cipherText)
        
        elif choice == '2':
            Text = input("Enter the text to decrypt: ")
            key = int(input("Enter the key (number of rails): "))
            decipherText = decipher(Text, key)
            print("Deciphered Text: "+decipherText)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def cipher(Text, key):
    result = ""
    matrix = [["" for x in range(len(Text))] for y in range(key)]
    increment = 1
    row = 0
    col = 0

    for c in Text:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[row][col] = c
        row += increment
        col += 1
    for list in matrix:
        result += "".join(list)
    return result
  
def decipher(Text, key):
    result = ""
    matrix = [["" for x in range(len(Text))] for y in range(key)]
    idx = 0
    increment = 1
    for selectedRow in range(len(matrix)):
        row = 0
        for col in range(len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += Text[idx]
                idx += 1
            row += increment

    matrix = transpose(matrix)
    for list in matrix:
        result += "".join(list)
    return result

def transpose(m):
    result = [[0 for y in range(len(m))] for x in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result

main()