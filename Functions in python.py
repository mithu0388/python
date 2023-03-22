#!/usr/bin/env python
# coding: utf-8

# ##Write a function to find the Max of three numbers.

# In[2]:


def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
print(max_of_three(100, 25, 250)) 


# ##Write a function to sum all the numbers in a list

# In[6]:


def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
my_list = [1, 2, 3, 4, 5]
result = sum(my_list)
print(result)


# ##Write a function to multiply all the numbers in a list

# In[8]:


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
list=[1,2,3,4,5]
result=multiply(list)
print(result)


# ##Write a function to reverse a string

# In[4]:


def reverse_string(input_string):
        char_list = list(input_string)
        char_list.reverse()
        reversed_string = ''.join(char_list)
        return reversed_string
print(reverse_string('python')) 


# ##Write a function to find the factorial of a number.

# In[21]:


def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
num = 5  
print("Factorial of",num,"is",)  
fact(num)


# ##Write a function that accepts a string and calculate the number of upper case letters and lower case letters

# In[16]:


def countupperlower(input_string):
    uppercount = 0
    lowercount = 0
    for char in input_string:
        if char.isupper():
            uppercount += 1
        elif char.islower():
            lowercount += 1
    return uppercount, lowercount
uppercount, lowercount =countupperlower ('India')
print('Number of upper case letters:', uppercount) 
print('Number of lower case letters:', lowercount) 


# ##Write a function that takes a list and returns a new list with unique element of the first list.

# In[5]:


def get_unique_elements(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list=[1, 2, 3, 2, 4, 1, 5, 6, 5]
unique_list = get_unique_elements(input_list)
print(unique_list) 


# In[ ]:




