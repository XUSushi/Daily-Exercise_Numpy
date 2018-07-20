
# coding: utf-8

# In[1]:

def foo(a,b):
    c=1
    d=a+b+c


# In[2]:

c#访问不到，因为出了作用域


# In[3]:

c=1 #全局作用域，不只是函数


# In[4]:

def foo(a,b):
    d=a+b+c


# In[6]:

c


# In[7]:

import numpy


# In[8]:

numpy.pi


# In[10]:

#class作用域
var = 0

class MyClass(object):
    # class variable
    var = 1
    
    def access_class_c(self):
        print('class var:', self.var)
    
    def write_class_c(self):
        MyClass.var = 2
        print('class var:', self.var)
        
    def access_global_c(self):
        print('global var:', var)
    
    def write_instance_c(self):
        self.var = 3
        print('instance var:', self.var) 


# In[11]:

pi


# In[14]:

import numpy


# In[15]:

from numpy import pi


# In[16]:

pi


# In[17]:

time.sleep(3)


# In[19]:

import time


# In[20]:

dir(time)


# In[21]:

time.sleep(3)#睡三秒再运行


# In[23]:

time.time()


# In[24]:

a1=time.time()


# In[25]:

s1=time.time()


# In[30]:

a1


# In[27]:

s1


# In[31]:

s2=time.time()


# In[32]:

s3=time.time()


# In[33]:

s3


# In[34]:

s2#可以看出两步操作之间的间隔


# In[35]:

s3-s2


# In[40]:

dt=time.datetime


# In[38]:

d1=datetime.data(2018,5,15)


# In[41]:

d1=dt.data(2018,5,15)


# In[42]:

import datetime as dt 


# In[43]:

d1 = dt.date(2007, 9, 25) #时间戳
d2 = dt.date(2008, 9, 25)


# In[44]:

d2


# In[45]:

print(d2.strftime('%A, %m/%d/%y'))#可以根据自己的喜好来表达日期


# In[46]:

print(d1.strftime('%a, %m-%d-%Y'))


# In[47]:

dt.datetime.now()#查看当前时间


# In[48]:

print(dt.datetime.now())#默认表现格式


# In[50]:

print(dt.datetime.now().strftime('%a, %m-%d-%Y'))#用自己定义的方式表现


# In[51]:

print(dt.datetime.now().strftime('%A, %m/%d/%y'))


# In[52]:

#function 一种对象类型


# In[53]:

foo


# In[55]:

map


# In[59]:

a=[1,3,5]


# In[58]:

b = map(square,a)


# In[60]:

lambda


# In[61]:

lambda x:x*x


# In[62]:

def square(x):return x*x


# In[63]:

#为啥要学csv,因为自然语言处理需要读取各种结构的数据


# In[65]:

data = [('one', 1, 1.5), ('two', 2, 8.0),('three',3,6.1)]
with open('out.csv', 'w') as fp:
    w = csv.writer(fp,lineterminator='\n') 
    w.writerows(data)

import csv
# In[66]:

data = [('one', 1, 1.5), ('two', 2, 8.0),('three',3,6.1)]
with open('out.csv', 'w') as fp:
    w = csv.writer(fp,lineterminator='\n') 
    w.writerows(data)


# In[67]:

import csv


# In[68]:

data = [('one', 1, 1.5), ('two', 2, 8.0),('three',3,6.1)]
with open('out.csv', 'w') as fp:
    w = csv.writer(fp,lineterminator='\n') 
    w.writerows(data)


# In[69]:

f.close()


# In[70]:

data1=[]


# In[72]:

f=open('out.csv','r')


# In[ ]:



