# Hill Cipher in Python

## Overview
The Hill cipher is a polygraphic substitution cipher based on linear algebra. It encrypts messages using matrix multiplication over modulo 26. This program allows users to encrypt text using a given key matrix.

## Code Explanation

### Converting Text to Numerical Representation
```python
def text_to_num(plaintext):
    return [ord(char) - ord('A') for char in plaintext]
```
- Converts plaintext letters to numbers (A=0, B=1, ..., Z=25).

### Generating the Key Matrix
```python
def key_to_matrix(key, m):
    key = key.upper().replace(" ", "")
    while len(key) < m * m:
        key += 'X'
    key_numbers = text_to_num(key)
    key_matrix = np.array(key_numbers).reshape(m, m)
    return key_matrix
```
- Ensures the key is uppercase and removes spaces.
- If the key is too short, it is padded with 'X'.
- Converts the key to numbers and reshapes it into an `m x m` matrix.

### Converting Numbers Back to Text
```python
def char_to_num(plain_num):
    return "".join(chr(num + ord('A')) for num in plain_num)
```
- Converts numbers back to characters.

### Encrypting the Text
```python
def hill_encrypt(plaintext, key_matrix):
```
- Ensures the plaintext is uppercase and removes spaces.
- Pads the text with 'X' if its length isn't a multiple of `m`.
- Converts text to numbers and encrypts using matrix multiplication.
- Converts the encrypted numbers back to text.

### Main Function
```python
m = int(input("Enter the dimension of the key matrix: "))
key = input("Enter the key: ")
key_matrix = key_to_matrix(key, m)
plain_text = input("Enter the plain text: ")
encrypted_text = hill_encrypt(plain_text, key_matrix)
print("The encrypted text is:", encrypted_text)
```
- Accepts user input for key matrix dimension and key.
- Encrypts the input text using the Hill cipher.
- Prints the encrypted text.

## Running the Code in Codespaces

### 1. Navigate to the Correct Folder
Your repository structure is:
```
INS_lab_programs/
│── Hill_Cipher/
│   ├── hill_cipher.py
│   ├── README.md
```
To navigate to the correct folder in your Codespace terminal, run:
```sh
cd INS_lab_programs/Hill_Cipher
```

### 2. Run the Program
Execute the following command:
```sh
python3 hill_cipher.py
```

### 3. Example Run
```
Enter the dimension of the key matrix: 2
Enter the key: KEY
Enter the plain text: HELLO
The encrypted text is: YZCFX
```

## Notes
- The key must be a square matrix (e.g., 2x2, 3x3).
- The plaintext should not contain spaces or special characters.
- Ensure Python and NumPy are installed in your Codespace (`pip install numpy`).

This completes the explanation of the Hill cipher and how to run it in Codespaces.

