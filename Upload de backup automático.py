#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyautogui')
get_ipython().system('pip install pyperclip')


# In[12]:


import pyautogui
import pyperclip
import time
pyautogui.alert("O código vai começar, não toque no computador")
pyautogui.PAUSE = 0.5
#abrir o google drive
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyperclip.copy("https://drive.google.com/drive/folders/10FX0XZLsfZmZi_0nGuyUKfQfI3ZF5joO")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")


#entrar na area de trabalho
pyautogui.hotkey("win","d")

#clicar no arquivo e arrastar ele
pyautogui.moveTo(x=116, y=343) #mover o mouse para  o arquivo
pyautogui.mouseDown() #clica e segura
pyautogui.moveTo(x=663, y=424)

#enquanto estou arrastando eu vou mudar para o google drive
pyautogui.hotkey("alt", "tab")
time.sleep(2)

#largar o arquivo no google drive
pyautogui.mouseUp() #largar o mouse
time.sleep(5)



#esperar 5 segundos


# In[9]:


time.sleep(3)
pyautogui.position()


# In[ ]:




