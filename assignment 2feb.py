#!/usr/bin/env python
# coding: utf-8

# 

# 1.

# For loop: A for loop is a control flow statement that executes code repeatedly for a particular number of iterations. In this control flow statement, the keyword used is for. The for loop is used when the number of iterations is already known.
# 
# ex:-
# 
# inputList = [10, 20, 30, 40, 50]
# 
# print("Input list elements:")
# 
# for element in inputList:
#    
#    print(element)
# 
# While loop: A loop that executes a single statement or a group of statements for the given true condition. The keyword used to represent this loop is "while". A "while" loop is used when the number of iterations is unknown. The statement repeats itself till the boolean value becomes false. In a while loop, the condition is tested at the start, also known as the pre-test loop.
# ex:-
# 
# 
# while i < 10:
# 
# print(i)
# 
# i += 1 
# 

# 2

# In[1]:


#using while loop

sum=0
product=1
i=1
while i<=10:
    sum=sum+i
    product=product*i
    i=i+1
print("sum of first 10 natural number is ",sum ,"and product is ",product)    


# In[2]:


#using for loop

sum=0
product=1
i=1
for i in range(1,11):
    sum=sum+i
    product=product*i
    
print("sum of first 10 natural number is ",sum ,"and product is ",product)    


# 3

# In[3]:


unit=int(input("enter the electricity consumed ->"))    
price=0
while True:
    
    if unit>300:
      price= price+(unit-300)*20
      unit=300
    elif unit>200 and unit<=300:
      price=price+(unit-200)*10
      unit=200
    elif unit>100 and unit<=200:
      price =price+(unit-100)*6
      unit=100
    elif unit>0 and unit<=100:
      price=price+unit*4.5
      break
print(price)


# 4

# In[4]:


list=list(range(1,101))


# In[5]:


list


# In[8]:


#using for loop
mul=[]

for i in list:
    cube=i**3
    if cube%4==0 and cube%5==0:
        mul.append(cube)
print(mul)        


# In[15]:


#using while loop

i=1
mul=[]
while i<101:
    cube=i**3
    if cube%4==0 and cube%5==0:
        mul.append(cube)
    i+=1    
print(mul)        


# In[16]:


5


# In[17]:


vow=["a","e","i","o","u"]
string="I want to become data scientist"


# In[ ]:





# In[44]:


#l_vow=[]
count=0
j=0
for i in string:
    for j in range(len(vow)):
        if i.lower()==vow[j]:
           # l_vow.append(i)
            count=count+1
       
print(count)        
        
   
    
    

