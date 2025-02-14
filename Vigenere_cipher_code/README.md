# Vigenère Cipher Implementation

## Introduction
This project implements the Vigenère Cipher, a classical method of encrypting and decrypting alphabetic text using a repeated key sequence. This cipher is a form of polyalphabetic substitution that improves security over simple Caesar ciphers by introducing a shifting key pattern.

## How the Code Works
The provided Python script enables both encryption and decryption using the Vigenère Cipher. Below is a step-by-step breakdown of the code:

### 1. Function Definition
The function `vigenere_cipher` takes three parameters:
- `key`: The string used to encrypt or decrypt the text.
- `plain_txt`: The input text to be encrypted or decrypted.
- `decrypt` (optional, default is `False`): A flag to determine whether to encrypt (`False`) or decrypt (`True`).

```python
 def vigenere_cipher(key, plain_txt, decrypt=False):
```
### 2. Key Expansion
Since the key needs to match the length of the text, it is repeated accordingly:
```python
 key = key * (len(plain_txt) // len(key) + 1)
```
### 3. Processing Each Character
The function loops through each character in `plain_txt`:
```python
 for i, ch in enumerate(plain_txt):
```
- If the character is alphabetic, the following operations take place:
  - The base ASCII value is determined (`A` for uppercase, `a` for lowercase):
  
    ```python
    base = (ord('A') if ch.isupper() else ord('a'))
    ```
  
  - The shift amount is computed based on the key:
  
    ```python
    shift_amt = shift * (ord(key[i].lower()) - ord('a'))
    ```
  
  - The new shifted character is appended to the result list:
  
    ```python
    result.append(chr((shift_amt + (ord(ch) - base)) % 26 + base))
    ```

- If the character is not alphabetic (e.g., numbers, punctuation), it is appended to the result unchanged.

### 4. Encryption and Decryption
The script sets the `shift` variable to `-1` if decrypting, otherwise `1`:
```python
 shift = -1 if decrypt else 1
```
This ensures that decryption reverses the encryption process by shifting in the opposite direction.

### 5. User Input
The user is prompted to enter:
- A key (string without spaces)
- A plaintext message to encrypt

```python
 key = input("Enter the key: ")
 plaintext = input("Enter the plaintext: ")
```

### 6. Encryption and Decryption Execution
- The text is first encrypted:
  
  ```python
  encrypted_text = vigenere_cipher(key, plaintext)
  ```
  
- Then, the encrypted text is decrypted back to its original form:
  
  ```python
  decrypted_text = vigenere_cipher(key, encrypted_text, decrypt=True)
  ```

### 7. Output
The program prints the encrypted and decrypted text:
```python
 print("Encrypted text:", encrypted_text)
 print("Decrypted text:", decrypted_text)
```
## Colab link to run the program
https://colab.research.google.com/drive/1ZbKL2mBdlbCBVVn5iCIeo0SkNdpO6suI?usp=sharing


## Example Run
### Input:
```
Enter the key: SECRET
Enter the plaintext: HELLO WORLD
```
### Output:
```
Encrypted text: ZIWWA XQKTW
Decrypted text: HELLO WORLD
```

## Notes
- The cipher only processes alphabetic characters.
- Spaces and punctuation remain unchanged.
- The key should be alphabetic and preferably long to increase security.

## Improvements
- Support for case-sensitive encryption.
- Handling of non-alphabetic characters in a more sophisticated manner.
- GUI or command-line enhancements for better usability.

## Conclusion
This script demonstrates a simple yet effective implementation of the Vigenère Cipher. It provides a basic encryption and decryption mechanism while allowing users to experiment with different keys to understand the cipher's working.

