#harcoding the inputs and easymethod
# import numpy as np

# def text_to_numbers(text):
#     return [ord(char) - ord('A') for char in text]

# def numbers_to_text(numbers):
#     return ''.join(chr(num + ord('A')) for num in numbers)

# def encrypt_hill_cipher(plaintext, key_matrix):
#     n = len(key_matrix)  # Matrix size (n x n)
#     plaintext = plaintext.upper().replace(" ", "")

#     # Padding if length is not a multiple of n
#     while len(plaintext) % n != 0:
#         plaintext += 'X'

#     plaintext_numbers = text_to_numbers(plaintext)
#     ciphertext_numbers = []

#     # Encrypt in chunks of size n
#     for i in range(0, len(plaintext_numbers), n):
#         vector = np.array(plaintext_numbers[i:i+n])
#         encrypted_vector = np.dot(key_matrix, vector) % 26
#         ciphertext_numbers.extend(encrypted_vector)

#     return numbers_to_text(ciphertext_numbers)

# # Example Usage
# key_matrix = np.array([[7,8],[11,11]])  # 3x3 matrix
# plaintext = "SHORT"

# ciphertext = encrypt_hill_cipher(plaintext, key_matrix)
# print("Ciphertext:", ciphertext)


##taking input from the user
import numpy as np

def text_to_num(plaintext):
    return [ord(char) - ord('A') for char in plaintext]

def key_to_matrix(key, m):
    key = key.upper().replace(" ", "")  # Ensure uppercase and remove spaces
    while len(key) < m * m:  # Pad key to match matrix size
        key += 'X'

    key_numbers = text_to_num(key)
    key_matrix = np.array(key_numbers).reshape(m, m)  # Reshape into m x m matrix
    return key_matrix

def char_to_num(plain_num):
    return "".join(chr(num + ord('A')) for num in plain_num)

def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]  # Matrix dimension
    cipher_num = []

    plaintext = plaintext.upper().replace(" ", "")  # Ensure uppercase and remove spaces
    while len(plaintext) % n != 0:  # Pad plaintext to match key matrix size
        plaintext += 'X'

    plain_num = text_to_num(plaintext)

    for i in range(0, len(plain_num), n):
        vector = np.array(plain_num[i:i + n])
        vector_mul = np.dot(key_matrix, vector) % 26
        cipher_num.extend(vector_mul)

    cipher_text = char_to_num(cipher_num)
    return cipher_text

# User input for matrix dimension and key
m = int(input("Enter the dimension of the key matrix: "))
key = input("Enter the key: ")

key_matrix = key_to_matrix(key, m)

plain_text = input("Enter the plain text: ")

encrypted_text = hill_encrypt(plain_text, key_matrix)

print("The encrypted text is:", encrypted_text)

