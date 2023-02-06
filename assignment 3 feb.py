#!/usr/bin/env python
# coding: utf-8

# # 1

#  def keyword is used to create afunction 

# In[1]:


def odd(n):
    odd=[]
    for i in range(n):
        if i%2!=0:
            odd.append(i)
    return odd        


# In[2]:


odd(25)


# 2

# *args=> it is used to pass multiple arguement in function 
# 
# **kwargs=> it is used to pass keyword arguement in the function

# In[3]:


def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)    


# In[4]:


sum(1,2,4,5,3,3)


# In[5]:


def kwargs(**kwargs):
    return kwargs    


# In[6]:


kwargs(name=['gaurav','ram','shyam','girdhar'],lname=['jangid','sharma','choudhary'])


# Iterator =>
# in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.
# 
# __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
# 
# __next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.
# 
# iterable and iterator are different. The main difference between them is, iterable cannot save the state of the iteration, but whereas in iterators the state of the current iteration gets saved.
# 
# Note: Every iterator is also an iterable, but not every iterable is an iterator in Python.
# 

# In[7]:


list = [2,4,6,8,10,12,14,16,18,20]
list_iterator = iter(list)

print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))


#  4
#  
#  a special kind of function that return a lazy iterator called a generator iterator. These are objects that you can loop over like a list.
#  

# yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object
# 

# In[8]:


def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"
 
     
obj = fun_generator()
 
print(type(obj))
 
print(next(obj))

print(next(obj))


#  5

# In[9]:


def Prime(n):

    if(n==1 or n==0):
       return False
    for i in range(2,(n//2)+1):
        if(n%i==0):
          return False
    else:
        yield i


# In[10]:


n=1000
for i in range(1,n+1):
     print(Prime(i))
    


#  6

# In[11]:


def fib(n):
    i=0
    a,b=0,1
    while i<n:
        yield a
        a,b=b,a+b
        
        
        
        


# In[14]:


fib=fib(1)


# In[15]:


print(next(fib))


# In[16]:


print(next(fib))


# In[17]:


print(next(fib))


# In[18]:


print(next(fib))
print(next(fib))


#  7

# In[19]:


compr=[i for i in 'pwskills']


# In[20]:


compr


#  8

# In[37]:


#palindrome
def pallindrome(str):
    a=str
    rev=a[::-1]
    while True:
        if a==rev:
            print("it is pallindrome")
            break
        else:
            print('it is not pallindrome')
            break
            
        


# In[38]:


a="nitin"
pallindrome(a)


# 9
# 

# In[42]:


[i for i in range(0,101)  if i%2!=0  ]


# In[ ]:




