# Diffie-Hellman Key Exchange Implementation

## Overview
This is a Python program that demonstrates the **Diffie-Hellman Key Exchange Algorithm**, a method used for securely exchanging cryptographic keys over a public channel.

## Prerequisites
Ensure you have Python installed on your system. You can check this by running:
```sh
python --version
```
If Python is not installed, download and install it from [python.org](https://www.python.org/).

## How the Code Works
The program follows these steps to implement the Diffie-Hellman Key Exchange:

### 1. **User Input:**
   - The program asks the user to input a **prime number (q)** and a **primitive root (a)** of that prime number.
   - Two users, **A and B**, input their private keys (**Xa** and **Xb** respectively).

### 2. **Public Key Calculation:**
   - The public key for **A** is calculated as:
     ```python
     Ya = pow(a, Xa, q)  # (a^Xa) % q
     ```
   - The public key for **B** is calculated as:
     ```python
     Yb = pow(a, Xb, q)  # (a^Xb) % q
     ```
   - These public keys are exchanged over the network.

### 3. **Shared Secret Key Computation:**
   - A computes the shared secret key using B’s public key:
     ```python
     ka = pow(Yb, Xa, q)  # (Yb^Xa) % q
     ```
   - B computes the shared secret key using A’s public key:
     ```python
     kb = pow(Ya, Xb, q)  # (Ya^Xb) % q
     ```
   - Since both calculations are mathematically equivalent, the computed **ka** and **kb** will be the same.

### 4. **Output:**
   - The program prints:
     - Public key of A
     - Public key of B
     - Common secret key computed by A
     - Common secret key computed by B
   - The shared secret key is the same for both A and B, ensuring secure communication.


## Link to execute code

https://colab.research.google.com/drive/1Xru3Mo2NZsLrCdKWlLc2h2pjcSLMJ7B9?usp=sharing

## Sample Input/Output
```
Enter prime no: 23
Enter primitive root no: 5
Enter private key of A: 6
Enter private key of B: 15
Public key of A is: 8
Public key of B is: 19
Common key of A is: 2
Common key of B is: 2
```

## Security Considerations
- The choice of **q (prime number)** and **a (primitive root)** is crucial for security.
- Private keys (**Xa** and **Xb**) should be chosen randomly and kept secret.
- This implementation does not include protection against **man-in-the-middle (MITM) attacks**, so additional cryptographic measures like digital signatures should be used in practice.

## License
This project is open-source and can be used freely for educational purposes.

