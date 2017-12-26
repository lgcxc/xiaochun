#-*- coding:utf-8 -*-

from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
driver.get("http://www.taobao.com")
driver.add_cookie({'name':'kry-free','value':'value-bbb'})

for cookie in driver.get_cookies():
    print('%s->%s'%(cookie['name'],cookie['value']))


driver.quit()