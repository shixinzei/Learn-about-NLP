
# coding: utf-8

# ## 简单爬虫与正则表达式应用
# 有个非常热门的自然语言处理垂直技术叫做**知识图谱**，知识图谱的构建需要依托于大量的实体和关系，很多这样的内容是可以从互联网上取到的。
# 
# 我们这里举一个最简单的应用，我们用正则表达式把搜狗百科的一些词条和解释抽取出来。

# In[39]:


# 引入爬虫工具库
# encoding: UTF-8
import requests as rq
import re


# In[67]:


# 发送请求
# page = rq.get("https://baike.sogou.com/v231013.htm")

page = rq.get("https://baike.baidu.com/item/nlp/25220#viewPageContent}")


# In[68]:


# 返回状态码正常
page.status_code


# In[69]:


print(page.encoding)


# In[77]:


print(page.text.encode('utf-8'))


# In[78]:


# 词条正则表达式抽取
title_pattern = re.compile(r'<title>(.*?)</title>')
print(title_pattern)


# In[79]:


title = title_pattern.search(page.text) 
print(title.group(1))


# In[81]:


# 词条正则表达式抽取
content_pattern = re.compile(r'<p>(.*?)</p>') 
contents = content_pattern.findall(page.text) 
print(contents)


# In[82]:


list(map(lambda x:re.sub("<a .*?>|<\\\/[ab]>", "",x), contents))

