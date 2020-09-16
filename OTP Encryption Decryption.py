#!/usr/bin/env python
# coding: utf-8


message = "IF"
message = [ord(str(i)) for i in message]

key = int('1010110',2)
key1 = int('0110001',2)

a = key^message[0]
b = key1^message[1]
print(bin(a)[2:].zfill(7))
a1 = (str(bin(a)[2:].zfill(7))+" "+str(bin(b)[2:].zfill(7)))

encoded = a1.split(" ")
#print(encoded)
encoded = [chr(int(i,2)) for i in encoded]
encoded = "".join(encoded)
print(encoded)



decoded = [bin(ord(i))[2:].zfill(7) for i in encoded]
print(str(chr((int(decoded[0],2)^key)))+str(chr((int(decoded[1],2)^key1))))





