#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#WebDriver提供execute_scipt()执行JavaScript

driver.set_window_size(800,600)
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

js = "window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(3)

driver.quit()

#执行js文件
# video = driver.find_element_by_xpath("/dev/video")
# driver.execute_script("return arguments[0].play",video)
