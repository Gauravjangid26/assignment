#!/usr/bin/env python
# coding: utf-8

# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
# 
# Q2. Name the four pillars of OOPs.
# 
# Q3. Explain why the __init__() function is used. Give a suitable example.
# 
# Q4. Why self is used in OOPs?
# 
# Q5. What is inheritance? Give an example for each type of inheritance.

# Q1. 

# classes and objects are the two main aspects of object-oriented programming.
# 
# Look at the following illustration to see the difference between class and objects:
# 
# class
# Fruit
# 
# objects
# 
# Apple
# 
# Banana
# 
# Mango
# 
# Another example:
# 
# class
# Car
# 
# objects
# 
# Volvo
# 
# Audi
# 
# Toyota
# 
# So, a class is a template for objects, and an object is an instance of a class.
# 
# When the individual objects are created, they inherit all the variables and methods from the class.
# 
# 

# In[3]:


# create class
class Bike:
    name = ""
    gear = 0

#object
bike1 = Bike()
bike2=Bike()


# Q2.

# In[4]:


four pillar of oops are:-
    1.encapsulation
    2.abstraction
    3.inheritance
    4.polymorphism


# Q3.
# 
# The Default __init__ Constructor in C++ and Java. Constructors are used to initializing the object’s state. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
# 
# ex:-
# 
# 
# 
# class Person:
# 
# 	# init method or constructor
# 	def __init__(self, name):
# 		self.name = name
# 
# 	# Sample Method
# 	def say_hi(self):
# 		print('Hello, my name is', self.name)
# 
# 
# p = Person('Nikhil')
# 
# p.say_hi()
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# ## Q4.
# 
# self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
# 
# The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

# Q5
# 
# 
# inheritancee is property to inherit property of their parents,bu this code reusabilty increases.
# it is similar like children inherit property of their oarents
# 
# types of inheritance:-
# 
# 1.single inheritance
# 
# ex:-
# class Person:
#  
# 
#     def __init__(self, name):
#         self.name = name
#  
# 
#     def getName(self):
#         return self.name
#  
#     def isEmployee(self):
#         return False
#  
#  
# class Employee(Person):
#  
#     def isEmployee(self):
#         return True
#  
#  
# 
# emp = Person("Geek1")  
# print(emp.getName(), emp.isEmployee())
#  
# emp = Employee("Geek2")  
# print(emp.getName(), emp.isEmployee())
# 
# 2.multiple inheritance
# 3.multilevel inheritance
# 4.hirarichal inheritance
# 5.hybrid inheritance
# 
# 

# In[ ]:




