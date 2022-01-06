#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd
import numpy as np


# In[107]:


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


# In[108]:


train.head()


# In[109]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# In[110]:


def transformar_sexo(valor):
    if valor == 'female':
        return 1
    else: 
        return 0 
train ['Sex_binario'] = train ['Sex'].map(transformar_sexo)
test ['Sex_binario'] = test['Sex'].map(transformar_sexo)


# In[111]:


train.head()


# In[112]:


variaveis = ['Sex_binario', 'Age']


# In[113]:


x = train[variaveis]
y = train['Survived']


# In[114]:


np.random.seed(0)
x_treino, x_valid, y_treino, y_valid = train_test_split(x, y, test_size = 0.5)


# In[115]:


x_treino.shape, x_valid.shape, y_treino.shape, y_valid.shape


# In[116]:


x_treino = x_treino.fillna(-1)
x_valid = x_valid.fillna(-1)


# In[117]:


modelo = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)
modelo.fit(x_treino, y_treino)


# In[118]:


p = modelo.predict(x_valid)


# In[119]:


np.mean(y_valid == p)


# In[120]:


p = (x_valid['Sex_binario']==1).astype(np.int64)
np.mean(y_valid == p)


# In[121]:


x_prev = test[variaveis]
x_prev = x_prev.fillna(-1)
x_prev.head()


# In[122]:


p = modelo.predict(x_prev)
p


# In[123]:


test.head()


# In[124]:


sub = pd.Series(p, index=test['PassengerId'], name='Survived')
sub.shape


# In[125]:


sub.to_csv("primeiro_modelo.csv", header=True)


# In[126]:


get_ipython().system('head -n10 primeiro_modelo.csv')


# In[ ]:





# In[ ]:





# In[ ]:




