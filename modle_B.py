#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 产品 手机
#class product():
#    size="6寸"
#    def __init__(self,color):
#        self.color=color
 #   def call(self):
 #       print("hello")
  #  def send_message(self):
 #       print("你有一个快递")

# 实例化
#phone1 = product("土豪金")
# 获取属性
#print(phone1.color)
#print(phone1.size)
# 调用方法
#phone1.call()
# 实例化
#phone1 = product("玫瑰红")
# 获取属性
#print(phone1.color)
#print(phone1.size)
# 调用方法
#phone1.call()

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