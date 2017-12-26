#-*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep,ctime
import os

print(ctime())

driver = webdriver.Firefox()
#找不到文件C:/Users/xuchun.chen/PycharmProjects/base/file/checkbox.html
# file_path = 'file:///'+ os.path.abspath('checkbox.html')
file_path = "http://www.baidu.com"
driver.get(file_path)

driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").click()

# driver.find_element_by_xpath(".//*[@id='3001']")

driver.find_elements_by_css_selector('input[type = checkbox]').pop().click()



