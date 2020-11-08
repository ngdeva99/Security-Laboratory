q=int(input("Enter large prime integer(q):"))
a=int(input("Enter primitive root(a):"))
xa=int(input("Enter Xa:"))
ya=(a**xa)%q
k=int(input("Enter the value of k:"))
m=int(input("Enter Message:"))
print("Public key (Ya):",ya)
S1=(a**k)%q
print("S1:",S1)
i=1
while True:
	x=(k*i)%(q-1)
	if x==1:
		break
	else:
		i=i+1
S2=i*(m-(xa*S1))%(q-1)
print("S2:",S2)
print("Signature(S1,S2):(",S1,",",S2,")")
V1=(a**m)%q
V2=((ya**S1)*(S1**S2))%q
print("V1:",V1)
print("V2:",V2)
print("\t*** Verifivation ***")
if V1==V2:
	print("Signature is valid")
else:
	print("Signature is not valid!!!")