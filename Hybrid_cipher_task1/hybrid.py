import numpy as np

# Vigenère Cipher
def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]  # Repeat key
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            encrypted_char = chr(((ord(text[i].upper()) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(text[i])  # Preserve spaces and symbols
    return "".join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            decrypted_char = chr(((ord(text[i].upper()) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(text[i])
    return "".join(decrypted_text)

# Rail Fence Cipher
def rail_fence_encrypt(text, rails):
    matrix = [['\n' for _ in range(len(text))] for _ in range(rails)]
    row, direction = 0, 1
    
    for i in range(len(text)):
        matrix[row][i] = text[i]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    encrypted_text = []
    for r in range(rails):
        encrypted_text.extend([matrix[r][c] for c in range(len(text)) if matrix[r][c] != '\n'])
    
    return "".join(encrypted_text)

def rail_fence_decrypt(text, rails):
    matrix = [['\n' for _ in range(len(text))] for _ in range(rails)]
    row, direction = 0, 1
    
    for i in range(len(text)):
        matrix[row][i] = '*'
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    
    index = 0
    for r in range(rails):
        for c in range(len(text)):
            if matrix[r][c] == '*' and index < len(text):
                matrix[r][c] = text[index]
                index += 1
    
    decrypted_text = []
    row, direction = 0, 1
    for i in range(len(text)):
        decrypted_text.append(matrix[row][i])
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    
    return "".join(decrypted_text)

# Hybrid Encryption
def hybrid_encrypt(plaintext, vigenere_key, rail_fence_rails):
    vigenere_cipher = vigenere_encrypt(plaintext, vigenere_key)
    final_cipher = rail_fence_encrypt(vigenere_cipher, rail_fence_rails)
    return final_cipher

# Hybrid Decryption
def hybrid_decrypt(ciphertext, vigenere_key, rail_fence_rails):
    rail_fence_decipher = rail_fence_decrypt(ciphertext, rail_fence_rails)
    original_text = vigenere_decrypt(rail_fence_decipher, vigenere_key)
    return original_text

# Example Usage
plaintext = input("Enter the plaintext: ")
vigenere_key = input("Enter the vigenere key: ")
rail_fence_rails = int(input("Enter the rail fence number: "))

encrypted_text = hybrid_encrypt(plaintext, vigenere_key, rail_fence_rails)
decrypted_text = hybrid_decrypt(encrypted_text, vigenere_key, rail_fence_rails)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
