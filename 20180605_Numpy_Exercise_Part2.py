
# coding: utf-8

# In[2]:

#Matplotlib 基础
#Matplotlib是一个类似Matlab的工具包


# In[3]:

#导入 matplotlib 和 numpy


# In[4]:

get_ipython().magic('pylab')


# In[5]:

#plot 二维图


# In[7]:

#当只给定 y 值，默认以下标为 x 轴：


# In[8]:

get_ipython().magic('matplotlib inline')
x = linspace(0, 2 * pi, 50)
plot(sin(x))


# In[9]:

#给定 x 和 y 值：


# In[10]:

plot(x, sin(x))


# In[11]:

#多条数据线：


# In[12]:

plot(x, sin(x),
    x, sin(2 * x))


# In[13]:

#使用字符串，给定线条参数：


# In[14]:

plot(x, sin(x), 'r-^')


# In[15]:

#scatter 散点图


# In[16]:

plot(x, sin(x), 'bo')


# In[17]:

#scatter 可以达到同样的效果


# In[18]:

scatter(x, sin(x))


# In[19]:

#只是因为默认的坐标轴不一样，所以图像看上去有一点区别，但无实质区别


# In[21]:

#scatter函数与Matlab的用法相同，还可以指定它的大小，颜色等参数：


# In[22]:

x = rand(200)
y = rand(200)
size = rand(200) * 30
color = rand(200)
scatter(x, y, size, color)
# 显示颜色条
colorbar()


# In[23]:

#坐标轴，标题，网格


# In[24]:

#设置坐标轴的标签和标题
plot(x, sin(x))
xlabel('radians')
# 可以设置字体大小
ylabel('amplitude', fontsize='large')
title('Sin(x)')


# In[28]:

plot(x, sin(x))
xlabel('radians')
# 可以设置字体大小
ylabel('amplitude', fontsize='normal')#观察字体区别
title('Sin(x)')


# In[29]:

#坐标轴，标题，网格
#可以设置坐标轴的标签和标题：


# In[30]:

plot(x, sin(x))
xlabel('radians')
# 可以设置字体大小
ylabel('amplitude', fontsize='large')
title('Sin(x)')


# In[31]:

#用 'grid()' 来显示网格：


# In[32]:

plot(x, sin(x))
xlabel('radians')
ylabel('amplitude', fontsize='large')
title('Sin(x)')
grid()


# In[ ]:



