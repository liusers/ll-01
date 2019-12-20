#!/usr/bin/env python
# -*- coding:utf-8 -*-

#class classAI():
    al=10
    def print_a(self):
        print(self.al)

# 类的实例化
#c = classAI()
c.print_a()

#from modle_B import product
# 实例化
#phone1 = product("土豪金")
# 获取属性
#print(phone1.color)
#print(phone1.size)
# 调用方法
#phone1.call()

#d = {"name":"小明"}
#t = {"sex":"男","age":18}
#d.update(t)
#print(d)


#import selenium
#from selenium import webdriver
#driver = webdriver.charome()

#  python 处理异常
import os

try:
    os.mkdir("ll-1")
except FileExistsError:
    print("文件夹已存在")
else:
    print("文件夹创建成功")
finally:
    print("创建文件夹完成")

print("sdfsdf")