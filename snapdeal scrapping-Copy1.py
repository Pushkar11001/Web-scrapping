#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[9]:


from bs4 import BeautifulSoup


# In[10]:


import requests


# In[11]:


url = "https://www.snapdeal.com/?utm_term=437025299421_104151711009_%7Bbidstrategy%7D&utm_campaign=brand_account_brandcat_cpt_1d_ftu&utm_source=earth_sembrand&utm_medium=snapdeal"


# In[12]:


allow = requests.get(url)


# In[13]:


print(allow)


# In[14]:


soup = BeautifulSoup(allow.text)


# In[15]:


Product_name = soup.select(".product_name")


# In[16]:


Product_name


# In[17]:


Product_Titles = []
Product_links = []


# In[18]:


for item in Product_name:
    Product_Titles.append(item.text)
    link = "https://www.snapdeal.com/?utm_term=437025299421_104151711009_%7Bbidstrategy%7D&utm_campaign=brand_account_brandcat_cpt_1d_ftu&utm_source=earth_sembrand&utm_medium=snapdeal"
    Product_links.append(link)


# In[19]:


Product_Titles


# In[20]:


import pandas as pd


# In[31]:


Products = pd.DataFrame(Product_Titles,columns=["Products"])


# In[22]:


Products


# In[51]:


mrp = soup.select (".mrp")


# In[25]:


mrp


# In[52]:


mrp_list = []


# In[53]:


for item in mrp:
    mrp_list.append(item.text)


# In[54]:


mrp_list


# In[61]:


ecommerce.to_csv("ecommerce.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




