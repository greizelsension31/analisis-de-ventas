#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importar librerias

import pandas as pd
import os 
import matplotlib.pyplot as plt
import re
import datetime as dt




# In[3]:


os.listdir('file')


# In[4]:


df= pd.DataFrame()


# In[5]:


files= os.listdir('file')
for x in files:
    files=pd.read_csv('file/'+x)
    df=pd.concat([files, df])


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.dtypes


# In[9]:


# conteo de valores null en los csv 
df['Order ID'].isnull().value_counts()



# In[10]:


#filtrar valores nulos  de el  dataframe 

df = df[df['Order ID'].notnull()]


# In[11]:


df.isnull().value_counts()


# In[12]:


# definir el tipo de cada variable
df.head()


# In[13]:


df=df[df['Product'] != 'Product']


# In[14]:


# transformando quantity ordered en entero
df['Quantity Ordered']=df['Quantity Ordered'].astype('int64')

# transformadno datos de price each en decimales 
df['Price Each']=df['Price Each'].astype('float')


# tranformando datos de order date en fecha 
df['Order Date']=pd.to_datetime(df['Order Date'])


# In[15]:


df.info()






# #     ANALISIS DE VENTAS

# # Cual fue el mes con la venta mas Alta  

# In[16]:


# primero realizamos preguntas

# extraer el mes  con el mentodo dt.month  que es para llamar el mes en una columna adicional.

df['Mes']=df['Order Date'].dt.month

# realizar la multiplicacion de precio con cantidad para ver cuanto por ventas 
df['Total_ventas']=df['Quantity Ordered']+df['Price Each']



# In[17]:


df.head()


# In[27]:


# subplot de graficos         tamano de la grafica 
fig, axes =plt.subplots(1,2, figsize=(16,7))

ax1=plt.subplot(1,2,1)
ax2=plt.subplot(1,2,2)
ax1.bar(df_mes['Mes'],df_mes['Total_ventas'])
ax2.plot(df_fecha['Total_ventas'])
# definir aqui todos los  valores  de la x en el grafico
ax1.set_xticks(df_mes['Mes'])

plt.show()


# In[67]:


df_mes


# In[22]:


# agrupacion por fecha 

df_fecha=df.groupby('Order Date').sum(numeric_only=True)


# In[23]:


# metodo de agrupacion por semana ' w' y  ' m ' seria por mes


df_fecha=df_fecha.resample('w').sum()
df_fecha


# In[ ]:





# In[ ]:




