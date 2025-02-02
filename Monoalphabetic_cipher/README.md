# Monoalphabetic Cipher in Java

## Overview
This Java program implements a Monoalphabetic Cipher, which is a substitution cipher where each letter in the plaintext is replaced with a corresponding letter from a fixed mapping (cipher alphabet). This implementation allows encryption and decryption of lowercase English letters.

## Code Explanation

### Importing Required Libraries
```java
import java.util.Scanner;
```
The `Scanner` class is imported to take user input from the console.

### Defining the Monoalphabetic Cipher Mapping
```java
static char[] plain={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
static char[] cipher={'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'};
```
- `plain` array represents the standard English alphabet.
- `cipher` array represents the substituted cipher alphabet.

### Encryption Method
```java
public static String encrypt(String s) {
    char ch[]=new char[(s.length())];
    for(int i=0;i<s.length();i++) {
        for(int j=0;j<26;j++) {
            if(plain[j]==s.charAt(i)) {
                ch[i]=cipher[j];
                break;
            }
        }
    }
    return (new String(ch));
}
```
- The function `encrypt` takes a plaintext string `s` as input.
- It iterates over each character of `s`, searches for the corresponding letter in the `plain` array, and replaces it with the corresponding letter from `cipher`.
- The encrypted string is returned.

### Decryption Method
```java
public static String decrypt(String s) {
    char ch[]=new char[(s.length())];
    for(int i=0;i<s.length();i++) {
        for(int j=0;j<26;j++) {
            if(cipher[j]==s.charAt(i)) {
                ch[i]=plain[j];
                break;
            }
        }
    }
    return (new String(ch));
}
```
- The function `decrypt` takes an encrypted string `s` as input.
- It iterates over each character of `s`, searches for the corresponding letter in the `cipher` array, and replaces it with the corresponding letter from `plain`.
- The decrypted string is returned.

### Main Method
```java
public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the string of your choice");
    String text=sc.next();
    String enc=encrypt(text);
    System.out.println("Encrypted text :"+enc);
    String dec=decrypt(enc);
    System.out.println("Decrypted text :"+dec);
}
```
- The `main` function:
  - Prompts the user to enter a string.
  - Calls `encrypt()` to generate the encrypted text.
  - Calls `decrypt()` to decrypt the text back to its original form.
  - Displays both encrypted and decrypted results.

## Running the Code in Replint

### Click on the link below to run the code in replint

https://replit.com/@RashmithaR/Java#src/main/java/Main.java

### click on run button to execute the program 


### Example Run
```
Enter the string of your choice:
hello
Encrypted text: tiggs
Decrypted text: hello
```

## Notes
- The program currently supports only lowercase letters. To support uppercase letters or special characters, modifications are needed.
- Ensure that Java is installed in your Codespace environment by running `java -version` and `javac -version`.



