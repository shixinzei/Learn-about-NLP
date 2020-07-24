
# coding: utf-8

# # 基本文本处理操作

# NLP处理的对象是文本字符串内容，大家需要熟悉一些基本的文本字符串操作，这里以python为例，帮大家复习以下的中英文字符串操作：
# * 替换
# * 截取
# * 复制
# * 连接
# * 分割
# * 排序
# * 比较
# * 查找
# * 包含
# * 大小写转换

# ### 1.清理与替换

# In[6]:


en_str = "    hello   world,   hello,   my name is wydxry!      "
print(en_str)


# In[7]:


en_str.strip()


# In[8]:


en_str.strip().lstrip()


# In[10]:


# 去空格及特殊符号  
en_str.strip().lstrip().rstrip('!') 


# In[11]:


# 字符串替换
en_str.replace('hello', 'hia')


# In[15]:


zh_str = "    大家好 ，   我叫午夜的行人 ，  "
print(zh_str)


# In[16]:


# 去空格及特殊符号  
zh_str.strip().lstrip().rstrip('，') 


# In[17]:


# 字符串替换
zh_str.strip().replace('午夜的行人', 'wydxry')


# In[20]:


# 删除
zh_str.strip().replace('大家好', '').replace('，','')


# ### 2.截取

# In[21]:


my_str = "大家好，我是午夜的行人，我在成都上学，你吃饭没呢？"


# In[23]:


# 从左往右index从0开始，可以用index进行切片(左闭右开)
my_str[0:3]


# In[25]:


# 从左往右index从0开始，可以用index进行切片(左闭右开)
my_str[4:4+7]


# In[26]:


# 从右往左index从-1开始，可以用index进行切片(左闭右开)
my_str[-1-5:-1]


# In[28]:


# 间隔截取 间隔为2
my_str[::2]


# In[29]:


# 翻转
my_str[::-1]


# ### 3.连接与分割

# In[31]:


str1 = "大家好，我是wydxry，真好！"
str2 = "大家好，我是午夜的行人，你吃饭没呢？"
# 字符串连接
str1+str2


# In[34]:


# 通过join的方式连接
strs = ['我是午夜的行人', "我是wydxry", "我是xxx，好high哟,感觉人生已经达到了高潮,感觉人生已经达到了巅峰"]
"；".join(strs)


# In[37]:


"  ".join(strs)


# In[38]:


# 通过split的方式切分
tmp_str = "我是午夜的行人；我是wydxry；我是毛，好high哟,感觉人生已经达到了高潮,感觉人生已经达到了巅峰"
tmp_str.split("；")


# In[39]:


tmp_str.split("是")


# ### 4.比较与排序

# In[40]:


en_strs = ['ABc', 'aCd', 'CdE', 'xYz']


# In[41]:


# 以字母序排列，注意是以返回值形态返回排序结果，不改变原list
sorted(en_strs)


# In[42]:


# 自定义排序方式
def sort_fun(x):
    return x[1].lower()

sorted(en_strs, key=sort_fun)


# In[43]:


sorted(en_strs, key=lambda x:x[2].lower())


# ### 查找与包含

# In[45]:


# 查找可以用index和find
zh_str = "我是午夜的行人；我是wydxry；我是毛毛，好high哟,感觉人生已经达到了高潮,感觉人生已经达到了巅峰"
print(zh_str)


# In[46]:


zh_str.index("wydxry")


# In[47]:


zh_str.index("午夜的行人")


# In[49]:


# 未查找到
zh_str.index("zl")


# In[52]:


# 未查到
zh_str.find("zl")


# In[54]:


# 已查到
zh_str.find("wydxry")


# ### 大小写与其他变化

# In[62]:


en_str = 'Hello, My Name IS Wydxry'
print(en_str)


# In[63]:


# 都变为小写字母
en_str.lower()


# In[64]:


# 都变为大写字母
en_str.upper()


# In[65]:


# 首字母大写
en_str.capitalize()


# In[66]:


help(str)

