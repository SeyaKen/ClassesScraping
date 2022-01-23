#!/usr/bin/env python
# coding: utf-8

# In[21]:


get_ipython().system('pip install selenium')


# In[22]:


get_ipython().system('pip install beautifulsoup4')
from bs4 import BeautifulSoup


# In[23]:


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
time.sleep(3)


# In[27]:


url_login = 'https://room.chuo-u.ac.jp/ct/home'
browser.get(url_login)
time.sleep(3)
print('ログインページにアクセスしました。')


# In[28]:


element = browser.find_element(By.ID, "username_input")
element.clear()
element.send_keys(USER)
element = browser.find_element(By.ID, "password_input")
element.clear()
element.send_keys(PASS)
print('フォームを送信')


# In[29]:


browser_form = browser.find_element(By.CLASS_NAME, "form-button")
time.sleep(3)
browser_form.click()
time.sleep(3)
print('情報を入力してログインボタンを押しました')


# In[30]:


url = 'https://room.chuo-u.ac.jp/ct/syllabus__search'
browser.get(url)
time.sleep(3)
print(url,':アクセス完了')


# In[31]:


import urllib.request as req


# In[32]:


from selenium.webdriver.support.select import Select


# In[33]:


dropdown = browser.find_element(By.NAME, 'pagelen') # ② select要素を取得
select = Select(dropdown)


# In[34]:


select.select_by_index(len(select.options)-1) 


# In[35]:


dropdown = browser.find_element(By.NAME, 'morg1') # ② select要素を取得
select = Select(dropdown)
select.select_by_index(3)


# In[202]:


class_list = []
for a in range(38):
    elem = browser.find_element(By.CLASS_NAME, 'stdlist')
    name = elem.text.replace('\u3000', '')
    name = name.replace(' ', '+')
    name = name.replace('\n', ':')
    name = name.replace('学部・研究科など+授業科目名+学期+曜日・時限+担当教員+配当年次+単位数:', '')
    name = name + ':'
    nu = 0
    for num in range(len(name)):
        kaiten = 0
        if name[num] == ':':
            name2 = name[nu:num].replace(':', '')
            nu = num
            kijun = 0
            mydict = {'major': 'a', "classname": 'a','when': 'a', 'days': 'a', "teacher": 'a', 'haitou': 'a',"credits": 'a'}
            for ah in range(len(name2)):
                if name2[ah] == '+' and kaiten == 0:
                    mydict['major'] = name2[kijun:ah].replace('+', '')
                    kijun = ah
                    kaiten = kaiten + 1
                elif name2[ah] == '+' and kaiten == 1:
                    mydict['classname'] = name2[kijun:ah].replace('+', '')
                    kijun = ah
                    kaiten = kaiten + 1
                elif name2[ah] == '+' and kaiten == 2:
                    mydict['when'] = name2[kijun:ah].replace('+', '')
                    kijun = ah
                    kaiten = kaiten + 1
                elif name2[ah] == '+' and kaiten == 3:
                    mydict['days'] = name2[kijun:ah].replace('+', '')
                    kijun = ah
                    kaiten = kaiten + 1
                elif name2[ah] == '+' and kaiten == 4:
                    mydict['teacher'] = name2[kijun:ah].replace('+', '')
                    kijun = ah
                    kaiten = kaiten + 1
                elif name2[ah] == '+' and kaiten == 5:
                    mydict['haitou'] = name2[kijun:ah].replace('+', '')
                    kijun = ah
                    kaiten = kaiten + 1
                elif kaiten == 6:
                    mydict['credits'] = name2[len(name2)-1:len(name2)]
                    kijun = ah
            class_list.append(mydict)        
    if a != 37:
        browser_form = browser.find_element(By.ID, "AFHasNext")
        browser_form.click()


# In[205]:


print(class_list[1851])


# In[ ]:




