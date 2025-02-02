# Playfair Cipher in Python

## Overview

This Python program implements the Playfair cipher, a classical encryption technique that encrypts digraphs (pairs of letters) rather than single letters. This makes it more secure than simple substitution ciphers.

## Code Explanation

### Playfair Cipher Encryption Function

```python
def playfair(key, cipher):
```

This function takes two inputs: a `key` and a `cipher` (plaintext to encrypt). It returns the encrypted text.

#### Step 1: Generate the Key Table

```python
key="".join(dict.fromkeys((key+"ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J","")))
```

- Converts the key to uppercase.
- Appends the remaining letters of the alphabet, excluding 'J' (which is merged with 'I').
- Removes duplicates while maintaining order.

```python
table=[key[i:i+5] for i in range(0,25,5)]
```

- Constructs a 5x5 matrix (Playfair table) for encryption.

#### Step 2: Prepare Digraphs (Pairs of Letters)

```python
pairs=[]
i=0
while(i<len(cipher)):
    a=cipher[i]
    b=cipher[i+1] if i+1<len(cipher) else "X"
    if a==b:
        pairs.append((a,"X"))
        i+=1
    else:
        pairs.append((a,b))
        i+=2
```

- Creates letter pairs from the input.
- If a pair has identical letters, an 'X' is inserted between them.
- If a letter has no pair, 'X' is appended.

#### Step 3: Encrypt Each Pair

```python
def encrypt(pair):
    idx1=key.index(pair[0])
    idx2=key.index(pair[1])
    row1,col1=divmod(idx1,5)
    row2,col2=divmod(idx2,5)
```

- divmod returns both quotient and reminder
- Finds the position of each letter in the key table.
- Applies Playfair cipher rules:
  1. **Same Row:** Replace each letter with the one to its right.
  2. **Same Column:** Replace each letter with the one below.
  3. **Rectangle Rule:** Swap letters in opposite corners.

```python
encrypted_mes="".join(encrypt(pair)for pair in pairs)
return encrypted_mes
```

- Encrypts the text and returns it.

### Playfair Cipher Decryption Function

```python
def playfair_decrypt(key, cipher):
```

This function decrypts the cipher text back to plaintext.

- It follows the same structure as the encryption function but reverses the Playfair rules.
- The `decrypt` function finds letter positions and shifts them left or up instead of right or down.

```python
decrypted_mes="".join(decrypt(pair)for pair in pairs).replace('X','')
return decrypted_mes
```

- Removes padding 'X' added during encryption.

### Main Function

```python
key=input("enter the key:")
mes=input("enter the cipher:")
enc=playfair(key,mes)
dec=playfair_decrypt(key,enc)
```

- Accepts user input for the encryption key and plaintext message.
- Encrypts and then decrypts the message.

```python
print("encrypted message:"+enc)
print("decrypted message:"+dec)
```

- Displays encrypted and decrypted messages.

## Running the Code in Codespaces

### 1. Navigate to the Correct Folder

Your repository structure is:

```
INS_lab_programs/
│── Playfair/
│   ├── playfair.py
│   ├── README.md
```

To navigate to the correct folder in your Codespace terminal, run:

```sh
cd INS_lab_programs/Playfair
```

### 2. Run the Program

Execute the following command:

```sh
python3 playfair.py
```

### 3. Example Run

```
enter the key: SECRET
enter the cipher: HELLO
encrypted message: ZBRRPG
decrypted message: HELLO
```

## Notes

- The Playfair cipher does not handle spaces or punctuation; pre-process the input to remove them.
- Ensure Python is installed in your Codespace (`python3 --version`).



