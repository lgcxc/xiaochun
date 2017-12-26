# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.126.com")
driver.implicitly_wait(10)

# driver.switch_to.frame('x-URS-iframe')
# driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')

driver.switch_to.frame('x-URS-iframe')

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
driver.switch_to.default_content()
time.sleep(100)

driver.quit()