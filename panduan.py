#-*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.126.com")
driver.implicitly_wait(10)

print("before login..........")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()


print("before login..........")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

# text = driver.find_element_by_id("spnUid").text
# print(text)

driver.quit()


