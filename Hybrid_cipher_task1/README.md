# Hybrid Cipher (Vigenère Cipher + Rail Fence Cipher)

## Introduction
This project implements a **Hybrid Cipher** by combining **Vigenère Cipher** (Substitution) and **Rail Fence Cipher** (Transposition). The goal is to enhance encryption security by leveraging the strengths of both ciphers.

- **Vigenère Cipher**: A polyalphabetic substitution cipher that uses a repeating key to shift letters in the plaintext.
- **Rail Fence Cipher**: A transposition cipher that arranges the text in a zig-zag pattern and reads it row-wise.

By first applying **Vigenère encryption** and then **Rail Fence transposition**, this hybrid approach ensures better security than using either method alone.

---

## Code Explanation
### 1. **Vigenère Cipher Implementation**

#### **Encryption (`vigenere_encrypt`)**
- The input plaintext is processed letter by letter.
- Each letter is shifted using a key character.
- The key is repeated to match the length of the plaintext.
- Spaces and symbols are preserved.

#### **Decryption (`vigenere_decrypt`)**
- The process is reversed by shifting the letters back using the key.
- The key is again repeated to match the text length.

### 2. **Rail Fence Cipher Implementation**

#### **Encryption (`rail_fence_encrypt`)**
- The text is placed in a zig-zag pattern across multiple rails.
- The text is then read row-wise to produce the ciphertext.

#### **Decryption (`rail_fence_decrypt`)**
- The number of rails determines the structure of the zig-zag.
- The ciphertext is placed into the pattern and read row-wise to reconstruct the original order.

### 3. **Hybrid Cipher Implementation**

#### **Encryption (`hybrid_encrypt`)**
1. Apply **Vigenère encryption** to plaintext.
2. Apply **Rail Fence encryption** to the result.
3. Output the final encrypted text.

#### **Decryption (`hybrid_decrypt`)**
1. Apply **Rail Fence decryption** first.
2. Apply **Vigenère decryption** to get the original plaintext.

---

## Running the Code in Codespaces
### **Step-by-Step Guide**

1. **Open the Codespaces environment**
   - Visit your GitHub repository by clicking on this: [INS_lab_programs](https://github.com/RashmithaRB/INS_lab_programs.git)
   - Open **Codespaces** using: [Codespace Link](https://musical-space-spoon-q7qg9p6r49wpf9667.github.dev/)

2. **Navigate to the correct directory**
   ```bash
   cd Hybrid_cipher_task1
   ```

3. **Run the Python script**
   ```bash
   python hybrid.py
   ```

4. **Provide Input**
   - Enter the plaintext message.
   - Provide a key for the Vigenère cipher.
   - Choose the number of rails for the Rail Fence cipher.

5. **Output Example**
   ```
   Enter the plaintext: THISISACECRET MESSAGE
   Enter the vigenere key: KHUSHI
   Enter the rail fence number: 10
   
   Plaintext: THISISACECRET MESSAGE
   Encrypted: DKOANCZYKWPGA KDJMYYU
   Decrypted: THISISACECRET MESSAGE
   ```

This confirms that the encryption and decryption work correctly.

---

## **Security Justification**
1. **Substitution (Vigenère Cipher)**: Prevents frequency analysis by using a polyalphabetic approach.
2. **Transposition (Rail Fence Cipher)**: Scrambles character positions, making patterns harder to detect.
3. **Hybrid Approach**: Enhances security by combining **both transformations**, making it more resistant to attacks.

---

## **Conclusion**
This hybrid cipher implementation strengthens encryption by combining **Vigenère and Rail Fence ciphers**. The project demonstrates how layering multiple ciphers enhances cryptographic security, making it harder for attackers to decrypt without both keys.

Feel free to modify the key length or rail count to experiment with different security levels!

---

### **Author**
GitHub: [RashmithaRB](https://github.com/RashmithaRB)

Happy coding! 🚀

