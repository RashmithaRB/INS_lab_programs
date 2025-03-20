import math
p=int(input("Enter the value of p "))
q=int(input("Enter the value of q "))
m=int(input("Enter the message integer "))
n=p*q
phi=(p-1)*(q-1)

#Function to calculate the GCD
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

#loop to check if an i value and phi have gcd equal to 1. if true then its considered as e
for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break

print("Public key (e, n):", (e, n))
  
C=pow(m,e,n)  #pow(Base, Exponent, Mod)
print("The encrypted message is: ",C)

d=pow(e,-1,phi)  #d is an integer which is the result of e inverse mod phi [also written as d=(phi*i+1)/e]
print("Private key (d, n):", (d, n))

M=pow(C,d,n)
print("The decrypted message is: ",M)
