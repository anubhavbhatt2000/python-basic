#!/usr/bin/env python
# coding: utf-8
loops example: Aeroplane landing program

# In[15]:


num = input("enter your alltitude:")

if num <= '1000':
  print('safe to land.')

elif num <= '4500':
    print(' assend to 1000 feet and try again')
    
elif num <= '6500':
    print('not safe to land go aroung and try again')
    

