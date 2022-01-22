#!/usr/bin/env python
# coding: utf-8

# In[93]:


get_ipython().system('pip install selenium')


# In[94]:


get_ipython().system('pip install beautifulsoup4')
from bs4 import BeautifulSoup


# In[95]:


from selenium.webdriver.common.by import By


# In[96]:


from selenium import webdriver
import time 
import pandas as pd


# In[97]:


USER = "20C3145009I"
PASS = "EB9Qak6UfLNKYG2"


# In[99]:


browser = webdriver.Chrome()
time.sleep(3)


# In[100]:


url_login = 'https://room.chuo-u.ac.jp/ct/home'
browser.get(url_login)
time.sleep(3)
print('ログインページにアクセスしました。')


# In[101]:


element = browser.find_element(By.ID, "username_input")
element.clear()
element.send_keys(USER)
element = browser.find_element(By.ID, "password_input")
element.clear()
element.send_keys(PASS)
print('フォームを送信')


# In[102]:


browser_form = browser.find_element(By.CLASS_NAME, "form-button")
time.sleep(3)
browser_form.click()
time.sleep(3)
print('情報を入力してログインボタンを押しました')


# In[103]:


url = 'https://room.chuo-u.ac.jp/ct/syllabus__search'
browser.get(url)
time.sleep(3)
print(url,':アクセス完了')


# In[106]:


import urllib.request as req


# In[107]:


from selenium.webdriver.support.select import Select


# In[108]:


dropdown = browser.find_element(By.NAME, 'pagelen') # ② select要素を取得
select = Select(dropdown)


# In[109]:


select.select_by_index(len(select.options)-1) 


# In[110]:


dropdown = browser.find_element(By.NAME, 'morg1') # ② select要素を取得
select = Select(dropdown)
select.select_by_index(1)


# In[161]:


class_list = []
for a in range(46):
    elem = browser.find_element(By.CLASS_NAME, 'stdlist')
    name = elem.text.replace('\u3000', '')
    name = name.replace(' ', ',')
    name = name.replace('\n', ':')
    name = name.replace('学部・研究科など,授業科目名,学期,曜日・時限,担当教員,配当年次,単位数:', '')
    name = name + ':'
    nu = 0
    for num in range(len(name)):
        if name[num] in ':':
            class_list.append(name[nu:num].replace(':', ''))
            nu = num
    if a != 45:
        browser_form = browser.find_element(By.ID, "AFHasNext")
        time.sleep(0)
        browser_form.click()


# In[166]:


print(class_list[2266])


# In[ ]:




