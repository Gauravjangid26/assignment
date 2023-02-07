#!/usr/bin/env python
# coding: utf-8

# # 1

# In[1]:


l=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[2]:


l.sort(key = lambda x: x[1])
print(l)
            


# # 2

# In[3]:


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[4]:


n_list=list(map(lambda i:i**2,l))


# In[5]:


print((n_list))


# # 3 

# In[6]:


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple=tuple(map(lambda i:str(i),l))


# In[7]:


tuple


# # 4 

# In[8]:


from functools import reduce
l=list(range(1,26))
l


# In[9]:


list(reduce(lambda x,y:x*y,l))


# # 5

# In[10]:


li=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


# In[11]:


new_list=list(filter(lambda x: x%2==0 and x%3==0  ,li))


# In[12]:


new_list


# # 6

# In[13]:


list1=['python', 'php', 'aba', 'radar', 'level']


# In[16]:


list2=list(filter(lambda x: x==x[::-1],list1))


# In[17]:


list2


# In[ ]:




