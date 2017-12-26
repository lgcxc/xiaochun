#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import os
import datetime

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

now = datetime.datetime.now()
time = now.strftime("%Y%m%d%H%M%S")
print(time)
driver.get_screenshot_as_file("C:/Users/xuchun.chen/PycharmProjects/base/file/baidu%s.png"%time)

driver.quit()