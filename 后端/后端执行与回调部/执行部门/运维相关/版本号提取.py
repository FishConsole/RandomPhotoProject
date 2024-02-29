# -*- coding: utf-8 -*-
import os

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 版本号提取():
    # 获取当前文件所在目录的绝对路径
    文件路径 = os.path.join(路径控制.前端资源目录().静态资源目录(), 'js', 'ChangeLog.js')
    # 读取JavaScript代码文件
    with open(文件路径, 'r', encoding='UTF-8') as f:
        f.readline()
        f.readline()
        原始文本 = f.readline()

    项目版本号 = 原始文本.split(':')[1]
    项目版本号 = eval(项目版本号.split(',')[0])

    return 项目版本号


def test版本号提取():
    print(版本号提取())
