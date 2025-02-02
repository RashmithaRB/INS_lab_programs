# Caesar Cipher Encryption & Decryption

## Introduction
This program implements the **Caesar Cipher** encryption and decryption algorithm in Python. The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions (key) in the alphabet.

## How It Works
The program consists of two functions:

1. `encrypt(plaintext, key)`: Encrypts the given text by shifting characters forward by `key` positions.
2. `decrypt(encrypted_text, key)`: Decrypts the text by shifting characters backward by `key` positions.

Both functions handle uppercase and lowercase letters separately and ensure non-alphabetic characters (like numbers, spaces, and punctuation) remain unchanged.

---

## Code Explanation

```python
# Function to encrypt the text

def encrypt(plaintext, key):
    encrypted_text = ""  # Initialize an empty string to store the encrypted result
    for i in plaintext:  # Iterate through each character in the input string
        if i.isalpha():  # Check if the character is a letter
            s = ord(i)  # Get ASCII value of the character
            if i.isupper():  # If uppercase letter
                ts = (s - ord('A') + key) % 26 + ord('A')  # Apply shift within uppercase range
            else:  # If lowercase letter
                ts = (s - ord('a') + key) % 26 + ord('a')  # Apply shift within lowercase range
            encrypted_text += chr(ts)  # Convert ASCII back to character and append to result
        else:
            encrypted_text += i  # Keep non-alphabet characters unchanged
    return encrypted_text  # Return the final encrypted text

# Function to decrypt the text

def decrypt(encrypted_text, key):
    decrypted_text = ""  # Initialize an empty string to store the decrypted result
    for i in encrypted_text:  # Iterate through each character in the encrypted string
        if i.isalpha():  # Check if the character is a letter
            s = ord(i)  # Get ASCII value of the character
            if i.isupper():  # If uppercase letter
                ts = (s - ord('A') - key) % 26 + ord('A')  # Reverse shift within uppercase range
            else:  # If lowercase letter
                ts = (s - ord('a') - key) % 26 + ord('a')  # Reverse shift within lowercase range
            decrypted_text += chr(ts)  # Convert ASCII back to character and append to result
        else:
            decrypted_text += i  # Keep non-alphabet characters unchanged
    return decrypted_text  # Return the final decrypted text

# Get input from user
in_text = input("Enter the string of your wish: ")
key = 3  # Define the shift key

# Encrypt the input text
encrypted_text = encrypt(in_text, key)
print('Encrypted text: ' + encrypted_text)

# Decrypt the text
decrypted_text = decrypt(encrypted_text, key)
print('Decrypted text: ' + decrypted_text)
```

### Explanation of Key Parts:
- **`ord(i)` and `chr()`**: Converts a character to its ASCII value and back.
- **Modulo (`% 26`)**: Ensures the shift wraps around within the English alphabet.
- **`isalpha()`**: Checks if a character is a letter.
- **Handles both uppercase and lowercase letters** separately for correct encryption/decryption.
- **Non-alphabet characters remain unchanged**.

---

## How to Run in GitHub Codespaces
To run this Python program in **GitHub Codespaces**, follow these steps:

### **1. Open GitHub Codespaces**
- Go to your GitHub repository containing this script.
- Click on the **"<> Code"** button, then go to the **Codespaces** tab.
- Click **"New Codespace"** (or open an existing one).

### **2. Install Python (If Not Installed)**
Run the following command in the terminal inside Codespaces:
```sh
python --version
```
If Python is not installed, install it using:
```sh
sudo apt update && sudo apt install python3 -y
```

### **3. Run the Python Script**
Once inside the Codespace terminal:
```sh
python caesar_cipher.py
```

### **4. Input & Output**
- Enter a message when prompted.
- The program will display the encrypted text.
- It will then decrypt the text back to the original message.

---

## Example Run
### **Input:**
```
Enter the string of your wish: Hello, World!
```

### **Output:**
```
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
```

---

## Conclusion
This project demonstrates a simple **Caesar Cipher** implementation in Python, using basic string manipulation and ASCII operations. It is a great introduction to encryption concepts and modular arithmetic.

---

**Contributors:** Rashmitha R Bangera  
**License:** MIT  
**Last Updated:** February 2025

