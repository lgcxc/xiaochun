#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
driver.get("http://www.taobao.com")

cookie = driver.get_cookies()
print(cookie)
print(cookie[0]['name'])

driver.quit()