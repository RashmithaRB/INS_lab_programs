def feistel(block, key, rounds=4):
    L, R = block[:len(block)//2], block[len(block)//2:]
    for i in range(rounds):
        L, R = R, ''.join(chr(ord(l) ^ ord(k)) for l, k in zip(L, key))
    return L + R

def encrypt(plaintext, key):
    return feistel(plaintext, key)

def decrypt(ciphertext, key):
    return feistel(ciphertext, key)

# Example usage
key = input("enter the key")
plaintext = input("enter the plaintext")
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
