#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath('upload.html')
driver.get(file_path)

#直接定位上传按钮，添加本地文件
driver.find_element_by_name('file').send_keys('C:\Users\\xuchun.chen\Desktop\up.txt')

time.sleep(3)

driver.quit()



