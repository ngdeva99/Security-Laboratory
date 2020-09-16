#!/usr/bin/env python
# coding: utf-8

# In[14]:


def encode(message,depth):
    
    c = len(message)//depth
    r = depth
    matrix = [[0 for _ in range(c)]for _ in range(depth)]
    enc = ""
    k = 0
    for i in  range(c):
        for j in range(r):
            if k!=len(message):
                matrix[j][i] = message[k]
                k+=1
            else:
                matrix[j][i] = 'O'
                
    for i in range(r):
        for j in range(c):
            
            enc+=matrix[i][j]
            
    return enc


# In[15]:


def decode(encmsg,depth):
    r = depth
    l = len(encmsg)
    c = l //depth
    k = 0
    mat= [[0 for _ in range(c)]for _ in range(depth)]
    dec = ""
    for i in range(r):
        for j in range(c):
            mat[i][j] = encmsg[k]
            k+=1

    for i in range(c):
        for j in range(r):
            dec += mat[j][i]
    return dec


# In[21]:



message = "IIT Madras, Chenna"
depth = 2
print("encoded: ",encode(message,depth))
print("decoded: ",decode("ITMda,CenI ars hna",depth))


# In[ ]:




