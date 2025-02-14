def vigenere_cipher(key,plain_txt,decrypt=False):
    result=[]
    shift= -1 if decrypt else 1
    key=key * (len(plain_txt)//len(key)+1)
    for i,ch in enumerate(plain_txt):
        if(ch.isalpha()):
            base=(ord('A')if ch.isupper() else ord('a'))
            #print(base)
            shift_amt=shift * (ord(key[i].lower())-ord('a'))
            #print(shift_amt)
            result.append(chr((shift_amt+(ord(ch)-base))%26+base))
            #print(''.join(result))
        else:
            result.append(ch)
    return ''.join(result).upper()
key=input("enter the key")
plaintext=input("enter the plaintext")
encrypted_text=vigenere_cipher(key,plaintext)
decrypted_text=vigenere_cipher(key,encrypted_text,decrypt=True)
print("Encryted text: ", encrypted_text)
print("Decrypted text: ",decrypted_text)
        
