#!/usr/bin/env python
# coding: utf-8

# # IF AND ELSE

# # nested elif
# 

# 1.with solid value

# In[ ]:


marks=30
if marks>=80 :
    print("you are on the A0 batch")
elif marks>=60 and marks<80 :
    print("you are on the A1 batch")
elif marks>=40 and marks<60 :
    print("you are on the A2 batch")
else :
    print("you are on the A3 batch")
    


# 2. with volatile value

# In[ ]:


marks= input("enter your marks") 


# In[ ]:


type(marks)


# In[ ]:


#only problem with input(), it return value in string
if marks>=80 :
    print("you are on the A0 batch")
elif marks>=60 and marks<80 :
    print("you are on the A1 batch")
elif marks>=40 and marks<60 :
    print("you are on the A2 batch")
else :
    print("you are on the A3 batch")
    


# In[ ]:


marks= int(input("enter your marks") )


# In[ ]:


if marks>=80 :
    print("you are on the A0 batch")
elif marks>=60 and marks<80 :
    print("you are on the A1 batch")
elif marks>=40 and marks<60 :
    print("you are on the A2 batch")
else :
    print("you are on the A3 batch")
    


# In[ ]:


# price=int(input("enter the price"))
if price > 1000:
    print("this no is greater than 1000 ")
    if price > 2000:
        print("this no is greater than 2000 ")
        if price > 3000:
            print("this no is greter than 3000")


# # iterative method
# 

# In[ ]:


l=[1,2,3,4,5,6,7,8]


# In[ ]:


for i in l:
    print(i)


# In[ ]:


for i in l:
    print(i+1)


# In[7]:


l1=[]
for i in l:
    i=i+1
    l1.append(i)


# In[ ]:


l=['gaurav','sanjay','ram']
l1=[]
for i in l:
    print(i)
    l1.append(i.upper())


# In[3]:


l=['gaurav','sanjay','ram']
l1=[]
for i in l:
    print(i)
    l1.append(i.upper())


# In[14]:


l=[1,23,4,53,"gaurav","shyam"]
lint=[]
lstr=[]
for i in l:
    if type(i)== int or type(i)== float():
        lint.append(i)
    else :
        lstr.append(i)


# In[15]:


lint


# In[16]:


lstr


# In[ ]:




