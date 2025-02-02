def encrypt(plaintext, key):
    encrypted_text = ""
    for i in plaintext:
        if i.isalpha():
            s = ord(i)
            if i.isupper():
                ts = (s - ord('A') + key) % 26 + ord('A')
            else:
                ts = (s - ord('a') + key) % 26 + ord('a')
            encrypted_text += chr(ts)
        else:
            encrypted_text += i  # Keep special characters unchanged
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in encrypted_text:
        if i.isalpha():
            s = ord(i)
            if i.isupper():
                ts = (s - ord('A') - key) % 26 + ord('A')
            else:
                ts = (s - ord('a') - key) % 26 + ord('a')
            decrypted_text += chr(ts)
        else:
            decrypted_text += i  # Keep special characters unchanged
    return decrypted_text

# Get input from user
in_text = input("Enter the string of your wish: ")
key = 3

# Encrypt and Decrypt
encrypted_text = encrypt(in_text, key)
print('Encrypted text: ' + encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print('Decrypted text: ' + decrypted_text)
