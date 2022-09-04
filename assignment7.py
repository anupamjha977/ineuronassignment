#!/usr/bin/env python
# coding: utf-8
1. Write a Python Program to find sum of array?
2. Write a Python Program to find largest element in an array?
3. Write a Python Program for array rotation?
4. Write a Python Program to Split the array and add the first part to the end?
5. Write a Python Program to check if given array is Monotonic?
# In[41]:


class Error(Exception):
    pass
class Notlist(Error):
    pass
def sum1(l):
    try:
        if (type(l)==list) is False:
            raise Notlist
        Sum=0
        for i in range(len(l)):
            Sum=Sum+l[i]
        return Sum
    except Notlist:
        print("Not a list please input a list")
   


# In[67]:


sum1([1,2,3,4])


# In[65]:


class Error(Exception):
    pass
class Notlist(Error):
    pass
def highestl(l):
    try:
        if (type(l)==list) is False:
            raise Notlist
        maximum =l[0]        
        for i in range(1,len(l)):
            if((l[i])>maximum):
                maximum=l[i]
        return maximum                           
    except Notlist:
        print("Not a list please input a list")


# In[56]:


highestl([1,2,3,4])


# In[57]:


highestl([10,9,4,3,1,5])


# In[66]:


highestl(2)


# In[14]:


#array rotation by temp
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr 


# In[15]:


rotateArray([1,2,3,4,5],5,2
           )


# In[18]:


class Error(Exception):
    pass
class Notlist(Error):
    pass

def rotateArray(arr,n,d):
    try:
        if (type(arr)==list) is False:
            raise Notlist
        arr[:]=arr[d:n]+arr[0:d]
        return arr
    except Notlist:
        print("Not a list please input a list")


# In[19]:


rotateArray([1,2,3,4,5,6],6,2)


# In[20]:


rotateArray(1,6,2)


# In[21]:


class Error(Exception):
    pass
class Notlist(Error):
    pass

def SplitArray(arr,n,d):
    try:
        if (type(arr)==list) is False:
            raise Notlist
        arr[:]=arr[d:n]+arr[0:d]
        for i in arr:
            print(i,end=" ")
    except Notlist:
        print("Not a list please input a list")


# In[22]:


SplitArray([1,2,3,4,5],5,2)


# In[23]:


# A array is Monotonic if it is either increasing or decreasing
def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


# In[25]:


isMonotonic([1,6,4,3])


# In[26]:


isMonotonic([9,8,7,6])


# In[ ]:




