#encoding:utf-8
from selenium import webdriver
import time
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://10.128.161.131/clid/software/clid/php/main.html")
print(driver.title)
time.sleep(3)

#登录操作

# driver.find_element_by_xpath("html/body/form/table/tbody/tr[1]/td[2]/input")
print("找到第一个input")
driver.find_elements_by_css_selector(".login").insert(1)
print("找到第一个input")




driver.quit()