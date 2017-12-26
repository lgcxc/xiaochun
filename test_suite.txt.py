# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')

print(driver.title)
# driver.find_element_by_name("wd").send_keys("read")
# driver.find_element_by_css_selector("#kw")
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.refresh()
driver.find_element_by_id("kw").clear()
time.sleep(2)
# driver.find_element_by_xpath(".//*[@id='su']")
# time.sleep(5)

driver.quit()