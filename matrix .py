#!/usr/bin/env python
# coding: utf-8

# In[15]:


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
c=[[9,8,7],
   [6,5,4],
   [3,2,1]]
d=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(0,len(d)):
   for j in range(0,len(d[0])):
    for k in range(0,len(c)):
         d[i][j]+=a[i][k]*c[k][i]
for row in d:
  print(row)

