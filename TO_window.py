# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

time.sleep(4)
# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('hao123').click()
# driver.find_element_by_link_text("登录").click()
# driver.find_element(by=By.LINK_TEXT, value="登录")


# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
time.sleep(5)

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("account").send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)
        # ……


driver.quit()