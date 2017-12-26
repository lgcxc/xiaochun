#encoding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://news.baidu.com/")
time.sleep(2)

# for i in range(5):
#     driver.find_element_by_xpath(".//*[@id='news']").click()
#     time.sleep(1)
#     de=driver.find_element_by_xpath(".//*[@id='newstitle']").click()

driver.find_element_by_xpath(".//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
print(driver.title)
driver.quit()