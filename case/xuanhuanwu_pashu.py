# coding: UTF-8
import time
from webbrowser import Chrome

from selenium import webdriver
# import pymouse, pykeyboard, os, sys
# from pykeyboard import PyKeyboard
# from pymouse import PyMouse
import json

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import unittest, pytest
from selenium.webdriver.common.keys import Keys
# import win32con, win32api
# m = PyMouse()
# k = PyKeyboard()
# url = 'https://pypi.org/project/pykeyboard/'
# # ds = DC.CHROME

# 创建一个txt文档，储存爬来的文字
txtWD = "C:\\Users\\Wshor\\Desktop\\星门.txt"
# 指定格式utf-8，否则有可能写入报错
txtWD2 = open(txtWD, 'w', encoding='utf-8')
# 玄幻屋
url = r'https://www.xuanhuanwu.com/'
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
# 进入
driver.get(url)
time.sleep(2)
# 输入书名
driver.find_element(By.ID, 'wd').send_keys('星门')
time.sleep(2)
# 搜索
driver.find_element(By.XPATH, '//*[@id="sform"]/div/span/input').click()
time.sleep(2)
# 把句柄切换到新页面
driver.switch_to.window(driver.window_handles[-1])
newPage = driver.current_window_handle
# 点击结果页第一条
driver.find_element(By.XPATH, '//*[@id="search-main"]/div[1]/ul/li[2]/span[2]/a').click()
time.sleep(2)
# 把句柄切换到新页面
driver.switch_to.window(driver.window_handles[-1])
newPage2 = driver.current_window_handle
time.sleep(3)
# 获取ul下有多少个li，即有多少章
ul = driver.find_element(By.XPATH, '//*[@id="list"]/div[3]/ul[2]')
lis = ul.find_elements(By.XPATH, 'li')
print(len(lis))
# first
title =driver.find_element(By.XPATH, '//*[@id="list"]/div[3]/ul[2]/li[1]/a')
# print(title.text)
txtWD2.write(title.text + '\n')
title.click()
time.sleep(2)
txt = driver.find_element(By.ID, 'txt')
# print(txt.text)
txtWD2.write(txt.text + '\n')
time.sleep(2)
# 下一章
for i in range(len(lis)-1):
    driver.find_element(By.ID, 'pb_next').click()
    time.sleep(1)
    title = driver.find_element(By.CLASS_NAME, 'chaptername')
    # print(title.text)
    txtWD2.write(title.text + '\n')
    txt = driver.find_element(By.ID, 'txt')
    # print(txt.text)
    txtWD2.write(txt.text + '\n')
    time.sleep(1)


# driver.close()



