#!/usr/bin/env python
# coding: utf-8

# In[1]:


for num in range(1,70264):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  


# In[ ]:




