# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
# driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://10.128.161.131/clid/software/clid/php/main.html')
# print("设置浏览器宽480、高800显示")
# driver.set_window_size(480, 800)
# driver.find_element_by_name("login").clear()
# driver.find_element_by_name("login").send_keys("read")
driver.find_element_by_class_name("button menu").click()
# driver.find_element_by_tag_name("input").send_keys("read")
# time.sleep(2)
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("read")
# time.sleep(5)
# driver.find_element_by_name("submitbuttonlogin").click()

driver.quit()