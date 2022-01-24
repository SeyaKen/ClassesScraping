#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from pprint import pprint


# In[3]:


get_ipython().system('pip install beautifulsoup4')
from bs4 import BeautifulSoup


# In[4]:


from selenium.webdriver.common.by import By


# In[5]:


from selenium import webdriver
import time 
import pandas as pd


# In[6]:


USER = "20C3145009I"
PASS = "EB9Qak6UfLNKYG2"


# In[7]:


browser = webdriver.Chrome()
time.sleep(3)


# In[8]:


url_login = "https://room.chuo-u.ac.jp/ct/home"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました。")


# In[9]:


element = browser.find_element(By.ID, "username_input")
element.clear()
element.send_keys(USER)
element = browser.find_element(By.ID, "password_input")
element.clear()
element.send_keys(PASS)
print("フォームを送信")


# In[10]:


browser_form = browser.find_element(By.CLASS_NAME, "form-button")
time.sleep(3)
browser_form.click()
time.sleep(3)
print("情報を入力してログインボタンを押しました")


# In[11]:


url = "https://room.chuo-u.ac.jp/ct/syllabus__search"
browser.get(url)
time.sleep(3)
print(url,":アクセス完了")


# In[12]:


import urllib.request as req


# In[13]:


from selenium.webdriver.support.select import Select


# In[14]:


dropdown = browser.find_element(By.NAME, "pagelen") # ② select要素を取得
select = Select(dropdown)


# In[15]:


select.select_by_index(len(select.options)-1) 


# In[19]:


class_list = {}
listt = [46, 29, 38, 34, 34, 18, 10, 5, 4]
kai = 0
for fdsa in range(1, 10):
    dropdown = browser.find_element(By.NAME, "morg1") 
    select = Select(dropdown)
    select.select_by_index(fdsa)
    L = listt[fdsa - 1]
    for a in range(L):
        elem = browser.find_element(By.CLASS_NAME, "stdlist")
        name = elem.text.replace("\u3000", "")
        name = name.replace(" ", "+")
        name = name.replace("\n", ":")
        name = name.replace("学部・研究科など+授業科目名+学期+曜日・時限+担当教員+配当年次+単位数:", "")
        name = name + ":"
        nu = 0
        for num in range(len(name)):
            kaiten = 0
            if name[num] == ":":
                name2 = name[nu:num].replace(":", "")
                nu = num
                kijun = 0
                kai += 1
                mydict = {"major": "a", "classname": "a","when": "a", "days": "a", "teacher": "a", "haitou": "a","credits": "a", "__collections__": {}}
                for ah in range(len(name2)):
                    if name2[ah] == "+" and kaiten == 0:
                        mydict["major"] = name2[kijun:ah].replace("+", "")
                        kijun = ah
                        kaiten = kaiten + 1
                    elif name2[ah] == "+" and kaiten == 1:
                        mydict["classname"] = name2[kijun:ah].replace("+", "")
                        kijun = ah
                        kaiten = kaiten + 1
                    elif name2[ah] == "+" and kaiten == 2:
                        mydict["when"] = name2[kijun:ah].replace("+", "")
                        kijun = ah
                        kaiten = kaiten + 1
                    elif name2[ah] == "+" and kaiten == 3:
                        mydict["days"] = name2[kijun:ah].replace("+", "")
                        kijun = ah
                        kaiten = kaiten + 1
                    elif name2[ah] == "+" and kaiten == 4:
                        mydict["teacher"] = name2[kijun:ah].replace("+", "")
                        kijun = ah
                        kaiten = kaiten + 1
                    elif name2[ah] == "+" and kaiten == 5:
                        mydict["haitou"] = name2[kijun:ah].replace("+", "")
                        kijun = ah
                        kaiten = kaiten + 1
                    elif kaiten == 6:
                        mydict["credits"] = name2[len(name2)-1:len(name2)]
                        kijun = ah

                class_list[f'{kai-1}'] = mydict        
        if a != L - 1:
            browser_form = browser.find_element(By.ID, "AFHasNext")
            browser_form.click()


# In[20]:


pprint(len(class_list))


# In[21]:


pprint(class_list)


# In[ ]:




