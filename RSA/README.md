# RSA Encryption & Decryption

## Overview
This project implements the **RSA algorithm** for encrypting and decrypting messages. RSA is a public-key cryptographic system that uses a pair of keys:
- **Public Key (e, n)**: Used for encryption
- **Private Key (d, n)**: Used for decryption

The code allows a user to input two prime numbers (`p` and `q`) and a message (integer) to perform encryption and decryption using RSA.

---
## How the Code Works

### 1. **Generate Key Pair**
#### Compute `n` and `phi(n)`
- The modulus `n` is calculated as:
  ```python
  n = p * q
  ```
- Euler's totient function `phi(n)` is:
  ```python
  phi = (p - 1) * (q - 1)
  ```

#### Choose Public Key `e`
- `e` must be **coprime** with `phi(n)`.
- We find the smallest `e` such that `gcd(e, phi) == 1`:
  ```python
  def gcd(a, b):
      while b:
          a, b = b, a % b
      return a

  for i in range(2, phi):
      if gcd(i, phi) == 1:
          e = i
          break
  ```
- The public key is **(e, n)**.

#### Compute Private Key `d`
- `d` is the modular inverse of `e` modulo `phi(n)`, calculated using:
  ```python
  d = pow(e, -1, phi)
  ```
- The private key is **(d, n)**.

---
## 2. **Encryption**
The encryption formula is:
```
C = (M^e) % n
```
Where:
- `M` is the plaintext (message as an integer)
- `C` is the ciphertext

**Code Implementation:**
```python
C = pow(m, e, n)
```
This computes `(m^e) % n` efficiently using modular exponentiation.

---
## 3. **Decryption**
The decryption formula is:
```
M = (C^d) % n
```
Where:
- `C` is the encrypted message
- `M` is the original plaintext

**Code Implementation:**
```python
M = pow(C, d, n)
```
This computes `(C^d) % n`, retrieving the original message.


---
## Example Execution
**Input:**
```
Enter the value of p: 11
Enter the value of q: 17
Enter the message in integer format: 88
```

**Output:**
```
Public key (e, n): (3, 187)
The encrypted message is: 12
Private key (d, n): (125, 187)
The decrypted message is: 88
```

---
## Explanation of Example
1. **Key Generation:**
   - `n = 11 * 17 = 187`
   - `phi = (11-1) * (17-1) = 160`
   - Smallest `e` such that `gcd(e, 160) = 1` is `3`
   - Compute `d = pow(3, -1, 160) = 125`
   - **Public Key:** `(3, 187)`
   - **Private Key:** `(125, 187)`

2. **Encryption:**
   - `C = (88^3) % 187 = 12`
   - Encrypted message: `12`

3. **Decryption:**
   - `M = (12^125) % 187 = 88`
   - Decrypted message matches original: `88`

---
## Summary
- The **public key (e, n)** is used for encryption.
- The **private key (d, n)** is used for decryption.
- The modular arithmetic and modular inverse are essential for RSA.
- This implementation demonstrates basic RSA encryption and decryption in Python.

---
## Notes
- The message must be converted to an **integer** before encryption.
- In real-world applications, **much larger prime numbers** (e.g., 1024-bit or 2048-bit) are used for security.



