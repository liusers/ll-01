#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 写入 W 先清空文件，后写入内容  a 文件末尾追加内容 b
# encoding="utf-8"  解决文件内写入中文时乱码的问题
#f = open("E:\\softwaredate\\python\\ll\\test.txt","w",encoding="utf-8")
# 写入内容 参数为字符串类型
#f.wirte("你好，啊啊")
# 写入内容，参数为list类型
#f.writelines(["123123123\n","324fees\n","dsgdges\n"])
#f.close()


# 读取内容 r读取模式
# encoding="utf-8"  解决文件读取内容时，中文乱码的问题
#f = open("test.txt","r",encoding="utf-8")
# 读取文件全部内容
#c = f.read()
#print(c)
# 按行读取文件全部内容
#lines = f.readlines()
#print(lines)
# 一次读取一行内容
# line = f.readline()
# print(line)
#f.close()


# with 是一个上下文管理器，with内的代码块在执行结束或者是执行出错的时候
#都会自动执行释放系统资源操作
#with open("test.txt","r",encoding="utf-8") as f:
#    c = f.read()
#    print(c)


import json
# json转字典
#j = '''
#{"name":"小明",
#"sex":"未知"
#}
#'''
#d = json.loads(j)
#d["sex"] = "男"
#print(d)
# 字典转json
#j = json.dumps(d,ensure_ascii=False)
#print(j)
# 获取随机数字
#import random
#a = random.randint(1,100)
#print(a)

# 有序得可迭代对象 str list tuple
#c = random.choice("sfdasdasfg")
#print(c)

import os
# 获取文件得绝对路径;_file_代表当前。py文件的绝对路径
#p = os.path.abspath("test.txt")
#print(p)
# 获取文件夹路径
#d = os.path.dirname(p)
#print(d)
# 获取文件名
#f = os.path.basename(p)
#print(f)

# 拼接目录跟文件
#path = os.path.join(d,f)
#print(path)
# 创建文件夹
#os.mkdir("ll-7")
