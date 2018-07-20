
# coding: utf-8

# In[1]:

from numpy import *


# In[2]:

dir(numpy)


# In[3]:

import numpy


# In[4]:

dir(numpy)


# In[5]:

from numpy import pi


# In[6]:

from numpy import array, sin


# In[7]:

a = [i for i in range(1,20)]


# In[8]:

a


# In[9]:

b = a * pi


# In[10]:

a = [i*pi for i in range(1,20)]


# In[11]:

a


# In[12]:

a_array = array(a)


# In[13]:

a_array


# In[14]:

dir(a_array)


# In[15]:

b = sin(a)


# In[16]:

b


# In[17]:

get_ipython().magic('matplotlib inline')


# In[18]:

plot


# In[19]:

from matplotlib import plot


# In[20]:

plot(a,b)


# In[21]:

import matplotlib.pyplot as plt


# In[22]:

plt.plot(a,b)


# In[23]:

help(linspace)


# In[24]:

x = linspace(0, 2*pi, 21)


# In[25]:

x


# In[26]:

y = sin(x)


# In[27]:

plt.plot(x,y)


# In[28]:

b = array([2,3,4,5])


# In[29]:

b+1


# In[30]:

b*pi


# In[31]:

a


# In[32]:

a*b


# In[33]:

a


# In[34]:

b


# In[35]:

a = b+1


# In[36]:

a


# In[37]:

a*b


# In[38]:

a**b


# In[39]:

a


# In[40]:

a[0]


# In[41]:

a.shape


# In[42]:

c = a + a


# In[43]:

c


# In[44]:

c.shape = 2,2


# In[45]:

c


# In[46]:

c.shape = 1,4


# In[47]:

c


# In[48]:

c.shape = 4,


# In[49]:

c


# In[50]:

d = cos(c)


# In[51]:

d


# In[52]:

c >= 10


# In[53]:

x = linspace(0, 2*pi, 21)


# In[54]:

x = linspace(0, 2*pi, 63)


# In[55]:

plt.plot(x, sin(x), x, sin(2*x))


# In[56]:

plt.plot(x, cos(x), 'r-')


# In[57]:

plt.plot(x, cos(x), 'r-^')


# In[58]:

plt.plot(x, sin(x),'b-o' x, sin(2*x),'r-^')


# In[59]:

plt.plot(x, sin(x),'b-o', x, sin(2*x),'r-^')


# In[60]:

help(numpy.rand)


# In[61]:

help(rand)


# In[62]:

from math import rand


# In[63]:

import random


# In[64]:

help(random.random)


# In[65]:

x = rand(200)


# In[66]:

x = random.random(200)


# In[67]:

x = array([i for i in range(1,50)])


# In[68]:

plt.plot(x, x**x)


# In[69]:

plt.plot(x,x**2)


# In[70]:

a


# In[71]:

a.dtype


# In[72]:

a.itemsize


# In[73]:

dir(a)


# In[74]:

a.nbytes


# In[75]:

a.dim


# In[76]:

a.ndim


# In[77]:

a.shape = 2,2


# In[78]:

a.ndim


# In[79]:

a


# In[80]:

a.shape = 4, 


# In[81]:

a


# In[82]:

a[1:3]


# In[83]:

a = array([1,2,3],[1,2,3],[1,2,3])


# In[84]:

a = array([[1,2,3],[1,2,3],[1,2,3]])


# In[85]:

a


# In[86]:

a.shape  


# In[87]:

a[1,3]


# In[88]:

a[1,1]


# In[89]:

a = array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])


# In[90]:

a


# In[91]:

a[2:4,:5 2]


# In[92]:

a[2:4]


# In[93]:

a[2:4,:]


# In[ ]:



