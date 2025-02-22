# README: Key Generation Code Explanation

## Overview
This script generates **8 different keys** by applying bitwise shifts and random bit removals to a given binary string. It uses **bitwise operations, random number generation, and list manipulations** to transform data systematically.

## Prerequisites
The script requires **Python 3.x** and uses the built-in `random` module.

## Code Explanation

### **Import Required Module**
```python
import random
```
- This imports Python’s `random` module, which is used to generate random numbers later in the script.

### **Asking the Input Binary String from user**
```python
s = input("Enter the string")  
```

```python
result = ''.join(format(ord(i),'08b') for i in s)
```
  - Convert each character of `s` into its **8-bit binary representation** using `ord(i)` and `format(ord(i), '08b')`.
  - Join these binary values into a single string.
  

### **Removing Every 8th Bit**
```python
answer = ""
for i in range(len(result)):
    if(i % 8 != 0):
        answer += result[i]
```
- This loop **removes every 8th bit** from `result`:
  - It iterates over all indices of `result`.
  - If an index is **not** a multiple of 8, the corresponding bit is added to `answer`.

### **Splitting the Binary String into Two Halves**
```python
l = int(len(answer) / 2)
left = answer[:l]
right = answer[l:]
```
- The `answer` string is split into two equal halves:
  - `left` contains the **first half**.
  - `right` contains the **second half**.

### **Defining Shift Values**
```python
lt = [2, 3, 6, 7, 1, 6, 5, 9]
```
- This list stores predefined **bit shift values** used to manipulate binary data.
- **These values are not fixed** and can be modified.

### **Initializing Storage for Keys**
```python
keys = []
```
- Creates an empty list `keys` to store the generated keys.

### **Generating the Keys**
```python
for i in range(0, 8):
```
- The loop runs **8 times**, once for each shift value in `lt`.

```python
    newKey = ""
    newAnswer = ""
```
- These variables store intermediate results.

```python
    nl = int(left, 2)
    nl = bin(nl << lt[i])
```
- Converts `left` (binary string) into an **integer**.
- Performs **left bitwise shift** by `lt[i]`.
- Converts the result back to a **binary string**.

```python
    num = 2 + lt[i]
```
- Defines `num`, which determines how much of the binary string is kept.

```python
    nr = int(right, 2)
    nr = bin(nr << lt[i])
```
- Performs the **same process** for the `right` half of the binary string.

```python
    newKey = nr[num:] + nl[num:]
```
- **Extracts and combines portions** of the shifted binary strings to form `newKey`.

### **Random Bit Removal**
```python
    rm = []
    while(len(rm) != 8):
        r = random.randint(0, len(newKey)-1)
        if(r not in rm):
            rm.append(r)
```
- **Selects 8 unique random indices** from `newKey` to remove bits.

```python
    for i in range(len(newKey)):
        if(i not in rm):
            newAnswer += newKey[i]
```
- **Removes bits** from `newKey` at the randomly chosen indices.

```python
    keys.append(newAnswer)
```
- Stores the final processed `newAnswer` in the `keys` list.

### **Printing the Keys**
```python
for i in range(0, len(keys)):
    print("Key ", i+1, " = ", keys[i])
```
- Iterates over `keys` and **prints** each generated key.

## Run the code in colab

https://colab.research.google.com/drive/1vLCAktczAGYtUIgj9W_6z-L45R0kQFRb?usp=sharing

## **Key Points**
1. **Bitwise Shift Operations**: `left` and `right` halves are shifted based on `lt` values.
2. **Random Bit Removal**: 8 random bits are removed from each transformed binary string.
3. **Key Generation**: The script produces 8 different keys based on the shifting and random bit removal process.
4. **Modifiability**: The values in `lt` **can be changed**, impacting how the keys are generated.

## **How to Modify the Code**
- **Change `lt` values** to modify shift patterns.
- **Adjust random bit removal logic** to control randomness.

## **Conclusion**
This script **demonstrates cryptographic transformations** using bitwise operations and random bit removal to create unique keys.

