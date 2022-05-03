#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install beautifulsoup4 


# In[4]:


pip install panda


# In[91]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import re
df = pd.read_excel(r'C:\Users\baijinpeng\Downloads\意大利线上竞争 (1).xlsx')
df


# In[92]:


df = df.drop(['Discount','RRP'],axis = 1)


# In[93]:


df


# In[96]:


Galaxy_A22_5G = df[df["PDT"] == "Galaxy A22 5G"]
Galaxy_A22_5G = Galaxy_A22_5G[Galaxy_A22_5G["SPEC"] == "4+64"]
Galaxy_A52s_5G = df[df["PDT"] == "Galaxy A52s 5G"]
Galaxy_A52s_5G = Galaxy_A52s_5G[Galaxy_A52s_5G["SPEC"] == "6+128"]
GT_Master_Edition = df[df["PDT"] == "GT Master Edition"]
GT_Master_Edition = GT_Master_Edition[GT_Master_Edition["SPEC"] == "6+128"]
moto_g60s = df[df["PDT"] == "Moto g60s"]
moto_g60s = moto_g60s[moto_g60s["SPEC"] =="6+128"]
A54s = df[df["PDT"] == "A54s"]


# In[97]:


A54s


# In[99]:


Galaxy_A22_5G.plot(x ='Day', y='Promo', kind = 'line', title = 'Samsung Galaxy A22 5G')
Galaxy_A52s_5G.plot(x ='Day', y='Promo', kind = 'line', title = 'Samsung Galaxy A52s 5G')
GT_Master_Edition.plot(x ='Day', y='Promo', kind = 'line', title = 'GT Master Edition')
moto_g60s.plot(x ='Day', y='Promo', kind = 'line', title = 'Motorola Moto g60s')
A54s.plot(x ='Day', y='Promo', kind = 'line', title = 'OPPO A54s')


# In[ ]:




