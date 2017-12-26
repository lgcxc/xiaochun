# coding:utf-8
from selenium import webdriver
import time
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")


# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(2)
# 删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(2)
# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(2)
# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(2)
# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()