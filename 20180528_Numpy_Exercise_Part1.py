
# coding: utf-8

# In[21]:

#Numpy 简介
#导入numpy
#Numpy是个重要的第三方库，有好多计算法
from numpy import *


# In[22]:

get_ipython().magic('pylab')


# In[3]:

#数组上的数学操作
a = [1, 2, 3, 4] #想通过这种形式将列表的每个元素加一，列表不支持这样的操作
a + 1
#会报错


# In[7]:

#将列表转化为array
a = array(a)#这个array函数就是numpy里的
a


# In[8]:

a+1#这样就可以成功了


# In[9]:

#array 数组支持每个元素加 1 这样的操作：


# In[10]:

#还可以与另一个 array 相加，得到对应元素相加的结果


# In[12]:

b = array([2, 13, 24, 9])
a+b#与另一个 array 的对应元素相加


# In[13]:

#对应元素相乘
a*b


# In[23]:

#修改数组形状
#查看array形状
c=[2,1,4,5]
d=array(c)
s=d.shape()#python 3 测试时会报错，没能成功


# In[24]:

#多维数组
w=array([[2, 4],
       [6, 8]])


# In[25]:

w*w


# In[26]:

#多维数组可以相乘


# In[27]:

#画图
#linspace 用来生成一组等间隔的数据：


# In[28]:

a = linspace(0, 2*pi, 21)
get_ipython().magic('precision 3')
a


# In[29]:

#三角函数：


# In[30]:

b = sin(a)
b


# In[31]:

#画出图像：
get_ipython().magic('matplotlib inline')
plot(a, b)


# In[32]:

#从数组中选择元素
#利用 b 产生一组布尔值：


# In[33]:

b >= 0


# In[34]:

mask = b >= 0


# In[35]:

#画出所有对应的非负值对应的点：


# In[36]:

plot(a[mask], b[mask], 'ro')


# In[ ]:



