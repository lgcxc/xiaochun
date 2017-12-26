# coding:utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.cn")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')

# texts = driver.find_elements_by_class_name("eACmFZ")
# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()
