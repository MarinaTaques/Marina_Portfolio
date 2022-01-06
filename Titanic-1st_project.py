#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[3]:


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


# In[5]:


train.head()


# In[62]:


from sklearn.ensemble import RandomForestClassifier


# In[9]:


modelo = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)


# In[13]:


train['Sex'].value_counts()


# In[ ]:


TREINO
VALIDACAO
TESTE


# In[25]:


def transformar_sexo(valor):
    if valor == 'female':
        return 1
    else: 
        return 0 
train ['Sex_binario'] = train ['Sex'].map(transformar_sexo)
test ['Sex_binario'] = test['Sex'].map(transformar_sexo)


# In[16]:


train.head()


# In[11]:


variaveis = ['Sex_binario', 'Age']


# In[26]:


x = train[variaveis]
y = train['Survived']


# In[19]:


x.head()


# In[20]:


y.head()


# In[29]:


x = x.fillna(-1)


# In[30]:


modelo.fit(x,y)


# In[40]:


x_prev = test[variaveis]
x_prev = x_prev.fillna(-1)
x_prev.head()


# In[42]:


p = modelo.predict(x_prev)
p


# In[43]:


test.head()


# In[56]:


sub = pd.Series(p, index=test['PassengerId'], name='Survived')
sub.shape


# In[53]:


sub.to_csv("primeiro_modelo.csv", header=True)


# In[54]:


get_ipython().system('head -n10 primeiro_modelo.csv')


# In[ ]:





# In[ ]:





# In[ ]:




