q=int(input("enter prime no: "))
a=int(input("enter primitive root no: "))
Xa=int(input("enter private key of A: "))
Xb=int(input("enter private key of B: "))
Ya=pow(a,Xa,q)
Yb=pow(a,Xb,q)
print("public key of A is: ",Ya)
print("public key of B is: ",Yb)
ka=pow(Yb,Xa,q)
kb=pow(Ya,Xb,q)
print("common key of A is: ",ka)
print("commom key of B is: ",kb)
