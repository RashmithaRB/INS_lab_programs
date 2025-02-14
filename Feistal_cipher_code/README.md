# Feistel Cipher Implementation

## Introduction
The Feistel cipher is a symmetric encryption technique that serves as the foundation for many block ciphers, such as DES. It divides the input data into two halves and processes them over multiple rounds using a round function and key.

This implementation provides both encryption and decryption using a lightweight Feistel cipher.

## How the Code Works
### 1. Function Definitions
#### Feistel Function
```python
def feistel(block, key, rounds=4):
```
- **block**: The input text (plaintext or ciphertext) divided into two halves.
- **key**: The encryption/decryption key.
- **rounds**: The number of Feistel rounds (default is 4).

**Process:**
- The input block is split into left (`L`) and right (`R`) halves.
- The Feistel function is applied iteratively.
- In each round, `L` becomes `R`, and `R` is XORed with the corresponding characters from the key.
- Finally, the concatenated result is returned.

#### Encryption Function
```python
def encrypt(plaintext, key):
    return feistel(plaintext, key)
```
Calls the `feistel` function to transform plaintext into ciphertext.

#### Decryption Function
```python
def decrypt(ciphertext, key):
    return feistel(ciphertext, key)
```
Since the Feistel structure is symmetric, applying the same function twice (with the same key) retrieves the original plaintext.

### 2. Example Usage
```python
key = "abcd"
plaintext = "hello!"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
```

### 3. Input and Output
#### Input:
```
Plaintext: hello!
Key: abcd
```
#### Output:
```
Ciphertext: encrypted_text
Decrypted Text: hello!
```

## COLAB LINK

https://colab.research.google.com/drive/146FzReWiZi6qg2zZduDWTbzEbMrjgjZ0?usp=sharing

## Key Features
- Simple and efficient implementation using string manipulations.
- Uses XOR operations for encryption and decryption.
- The same function is used for both encryption and decryption.
- The number of rounds can be adjusted for increased security.

## Limitations
- This is a basic Feistel implementation without complex round functions.
- The key length must match the left half of the block for proper execution.

## Conclusion
This implementation of the Feistel cipher provides a fundamental understanding of the structure used in real-world cryptographic algorithms. While simple, it demonstrates how a symmetric encryption scheme operates efficiently.

