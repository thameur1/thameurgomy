#!/usr/bin/env python
# coding: utf-8

# In[38]:


for x in range ( 2000,3200) :
    if (x % 7==0) and (x % 5 !=0) :
        print(x, end=" ")



# In[40]:


Res= 1 
x= int(input ("X"))
for i in range (1,x+1) :
    Res= Res*i
print(Res)


# In[21]:


n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)


# In[23]:


mot=input("tapez un mot")
liste1=list(mot)
ind=input(" tapez un indice")
ind=int(ind)
del(liste1[ind])
monmot="".join(liste1)
print(monmot)


# In[24]:


import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
print(x.tolist())


# In[25]:


import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nCross-correlation of the said arrays:\n",np.cov(x, y))


# In[37]:


from math import *
D=input( " tapez la valeur de D ")
D=int(D)
C=50
H=30
Q = sqrt(2*C*D/H)
print ( " la valeur de Q est",Q)


# In[ ]:




