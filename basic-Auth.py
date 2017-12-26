#-*- coding:utf-8 -*-
import random

verify = random.randint(100, 888)
print(u"随机数：%d" % verify)

number = input("请输入随机数：")
print(number)
number = int(number)

if number == verify:
    print("ok")
elif number == 1212:
    print("not")
else:
    print("sorry")

