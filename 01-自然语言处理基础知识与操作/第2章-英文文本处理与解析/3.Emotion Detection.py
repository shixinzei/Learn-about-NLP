
# coding: utf-8

# # 简易情感分析
# 
# 我们来结合一下sklearn，pandas和刚讲过的工具库，来构建一个简易情感分析模型。

# In[1]:


import numpy as np
import pandas as pd


# ## 加载数据

# In[2]:


data = pd.read_csv("./data/emotion_data.csv")


# In[3]:


data.shape


# In[4]:


data.head()


# In[5]:


# 不同的情感种类
data.sentiment.unique()


# ## 数据预处理

# In[6]:


# 去掉无关列
data = data.drop(data.columns[[0,2]], axis=1)


# In[7]:


data.head()


# In[10]:


# dataset = data.as_matrix() 失效
dataset = data.iloc[:,:].values


# In[11]:


dataset.shape


# In[14]:


features = dataset[:,1]
print(features.shape)


# In[15]:


features[123]


# In[16]:


target = dataset[:,0]


# In[17]:


# 使用LabelEncoder对不同的情感target进行编码
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
target_processed = le.fit_transform(target)


# In[18]:


le.classes_


# In[19]:


# 对输入的文本进行特征抽取和表示(这里用到的tf-idf特征在后面的课程中会讲到)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X_processed = tfidf.fit_transform(features)


# In[20]:


X_processed


# In[21]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_processed, target_processed, test_size=0.5, random_state=42)


# In[22]:


y_train


# In[24]:


X_train.shape


# ## 模型训练

# In[25]:


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)


# In[26]:


# 模型评估
lr.score(X_test, y_test)


# In[27]:


# 模型预测
test_ex = ["It is so horrible"]
text_ex_processed = tfidf.transform(test_ex)
lr.predict(text_ex_processed)


# In[28]:


print(lr.predict(text_ex_processed))

