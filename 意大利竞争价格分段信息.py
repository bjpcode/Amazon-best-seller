#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install beautifulsoup4 


# In[3]:


pip install panda


# In[141]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import re
df = pd.read_excel(r'C:\Users\baijinpeng\Downloads\意大利线上竞争 (1).xlsx')
df = df.drop(['Discount','RRP'],axis = 1)
df


# In[142]:


Range_0_100 = df[(df['Promo'] < 100)]
Range_100_150 = df[(df['Promo'] < 150)]
Range_100_150 = Range_100_150[(Range_100_150['Promo'] > 100)]
Range_150_200 = df[(df['Promo'] < 200)]
Range_150_200 = Range_150_200[(Range_150_200['Promo'] > 150)]
Range_200_250 = df[(df['Promo'] < 250)]
Range_200_250 = Range_200_250[(Range_200_250['Promo'] > 200)]
Range_250_295 = df[(df['Promo'] < 295)]
Range_250_295 = Range_250_295[(Range_250_295['Promo'] > 250)]
Range_295_360 = df[(df['Promo'] < 360)]
Range_295_360 = Range_295_360[(Range_295_360['Promo'] > 295)]
Range_360_410 = df[(df['Promo'] < 410)]
Range_360_410 = Range_360_410[(Range_360_410['Promo'] > 360)]
Range_410_570 = df[(df['Promo'] < 570)]
Range_410_570 = Range_410_570[(Range_410_570['Promo'] > 410)]
Range_570_up = df[(df['Promo'] > 570)]


# In[143]:


#range 100-150
Samsung_100_150 = Range_100_150[Range_100_150["Brand"] == "Samsung"]
realme_100_150 = Range_100_150[Range_100_150["Brand"] == "Realme"]
motorola_100_150 = Range_100_150[Range_100_150["Brand"] == "Motorola"]
#range 150-200
Samsung_150_200 = Range_150_200[Range_150_200["Brand"] == "Samsung"]
motorola_150_200 = Range_150_200[Range_150_200["Brand"] == "Motorola"]
OPPO_150_200 = Range_150_200[Range_150_200["Brand"] == "OPPO"]
#range 200-250
Samsung_200_250 = Range_200_250[Range_200_250["Brand"] == "Samsung"]
realme_200_250 = Range_200_250[Range_200_250["Brand"] == "Realme"]
OPPO_200_250 = Range_200_250[Range_200_250["Brand"] == "OPPO"]
#range 250-295
Samsung_250_295 = Range_250_295[Range_250_295["Brand"] == "Samsung"]
realme_250_295 = Range_250_295[Range_250_295["Brand"] == "Realme"]
#range 295-360
Samsung_295_360 = Range_295_360[Range_295_360["Brand"] == "Samsung"]
realme_295_360 = Range_295_360[Range_295_360["Brand"] == "Realme"]
OPPO_295_360 = Range_295_360[Range_295_360["Brand"] == "OPPO"]
#range 360-410
motorola_360_410 = Range_360_410[Range_360_410["Brand"] == "Motorola"]
realme_360_410 = Range_360_410[Range_360_410["Brand"] == "Realme"]
OPPO_360_410 = Range_360_410[Range_360_410["Brand"] == "OPPO"]
#range 410-570
motorola_410_570 = Range_410_570[Range_410_570["Brand"] == "Motorola"]
#range 570 up
apple_570_up = Range_570_up[Range_570_up["Brand"] == "Apple"]


# In[144]:


Range_100_150


# In[145]:


Range_150_200


# In[ ]:




