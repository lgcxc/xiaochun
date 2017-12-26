# coding:utf-8
from selenium import webdriver
import time

from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\Users\\xuchun.chen\AppData\Local\Google\Chrome\User Data\Default') #设置成用户自己的数据目录
driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.taobao.com/')