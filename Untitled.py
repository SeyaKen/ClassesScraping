#!/usr/bin/env python
# coding: utf-8

# In[22]:


get_ipython().system('pip install selenium')


# In[51]:


get_ipython().system('pip install beautifulsoup4')
from bs4 import BeautifulSoup


# In[32]:


from selenium.webdriver.common.by import By


# In[24]:


from selenium import webdriver
import time 
import pandas as pd


# In[25]:


USER = "20C3145009I"
PASS = "EB9Qak6UfLNKYG2"


# In[26]:


browser = webdriver.Chrome()
browser.implicitly_wait(3)


# In[27]:


url_login = 'https://room.chuo-u.ac.jp/ct/home'
browser.get(url_login)
print('ログインページにアクセスしました。')


# In[33]:


element = browser.find_element(By.ID, "username_input")
element.clear()
element.send_keys(USER)
element = browser.find_element(By.ID, "password_input")
element.clear()
element.send_keys(PASS)
print('フォームを送信')


# In[38]:


browser_form = browser.find_element(By.CLASS_NAME, "form-button")
browser_form.click()
print('情報を入力してログインボタンを押しました')


# In[39]:


url = 'https://room.chuo-u.ac.jp/ct/syllabus__search'
browser.get(url)
print(url,':アクセス完了')


# In[40]:


import urllib.request as req


# In[41]:


from selenium.webdriver.support.select import Select


# In[44]:


dropdown = browser.find_element(By.NAME, 'pagelen') # ② select要素を取得
select = Select(dropdown)


# In[45]:


select.select_by_index(len(select.options)-1) 


# In[47]:


dropdown = browser.find_element(By.NAME, 'morg1') # ② select要素を取得
select = Select(dropdown)
select.select_by_index(1)


# In[59]:


class_list = []
for num in range(49):
    elem = browser.find_element(By.CLASS_NAME, f'row{num % 2}')
    name = elem.text
    class_list.append(name)


# In[60]:


print(class_list)


# In[ ]:




