# Feistel Cipher Implementation

This repository contains a simple implementation of the Feistel cipher in Python. The Feistel cipher is a symmetric structure used in the construction of block ciphers. It splits the plaintext into two halves and processes them through multiple rounds of encryption and decryption.

## Code Explanation

### feistel_round Function

```python
def feistel_round(L, R, K):
    """
    One round of the Feistel cipher.
    Uses a simple round function: f(R, K) = (sum of ASCII values of R + K) % 256.
    Then, new_R = L XOR f(R, K).
    """
    new_L = R  # The right half becomes the new left half.
    round_function = (sum(ord(c) for c in R) + K) % 256  # Sum ASCII values of R and add key
    new_R = "".join(chr(ord(L[i]) ^ round_function) for i in range(len(L)))  # XOR operation
    return new_L, new_R
```

This function performs one round of the Feistel cipher. It takes three arguments: `L` (left half of the data), `R` (right half of the data), and `K` (round key). The round function used here is a simple sum of the ASCII values of the characters in `R` plus the key `K`, modulo 256. The new right half is obtained by XORing the left half with the result of the round function.

### feistel_encrypt Function

```python
def feistel_encrypt(plaintext, round_keys):
    """
    Encrypts a string plaintext using Feistel cipher with given round keys.
    """
    if len(plaintext) % 2 != 0:  # Ensure even length
        plaintext += "X"

    L, R = plaintext[:len(plaintext)//2], plaintext[len(plaintext)//2:]  # Split into two halves

    for K in round_keys:  # Apply multiple Feistel rounds
        L, R = feistel_round(L, R, K)

    return L + R  # Concatenate final halves as ciphertext
```

This function encrypts a plaintext string using the Feistel cipher with the provided round keys. If the plaintext length is odd, an extra character "X" is appended to make it even. The plaintext is then split into two halves, and multiple Feistel rounds are applied using the round keys. The final halves are concatenated to form the ciphertext.

### feistel_decrypt Function

```python
def feistel_decrypt(ciphertext, round_keys):
    """
    Decrypts a string ciphertext using Feistel cipher.
    Uses the round keys in reverse order.
    """
    L, R = ciphertext[:len(ciphertext)//2], ciphertext[len(ciphertext)//2:]  # Split into two halves

    for K in reversed(round_keys):  # Reverse the encryption rounds
        R, L = feistel_round(R, L, K)  # Reverse the Feistel process

    return (L + R).replace("X","")  # Concatenate to get the original plaintext
```

This function decrypts a ciphertext string using the Feistel cipher. It uses the round keys in reverse order to reverse the encryption process. The ciphertext is split into two halves, and multiple Feistel rounds are applied in reverse order. The final halves are concatenated to get the original plaintext, and any extra "X" added during encryption is removed.

### Example Usage

```python
round_keys = [3, 7, 2, 5]  # Example round keys
plaintext = "HELLO"  # Example plaintext
encrypted_text = feistel_encrypt(plaintext, round_keys)
decrypted_text = feistel_decrypt(encrypted_text, round_keys)
print(f"Plaintext: {plaintext}")          # Expected: HELLO
print(f"Ciphertext: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
```

This example demonstrates the usage of the Feistel cipher functions. It defines a list of round keys and a plaintext string. It then encrypts the plaintext, decrypts the resulting ciphertext, and prints the original plaintext, ciphertext, and decrypted text.

## How to run using colab
### Click on the below link

https://colab.research.google.com/drive/146FzReWiZi6qg2zZduDWTbzEbMrjgjZ0?usp=sharing

## How to Run using codespace

1.Navigate to codespaces created in repository
2. Ensure you have Python installed on your system.
3. Navigate the code to a file, e.g., `feistel_cipher.py`.
4. Run the script using the command:
   ```sh
   python feistel_cipher.py
   ```

## Conclusion

The provided implementation demonstrates a simple Feistel cipher with basic round functions. This can be extended and modified for more complex encryption schemes.




