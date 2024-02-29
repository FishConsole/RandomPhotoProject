# -*- coding: utf-8 -*-
import os


def 版本号提取():
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接绝对路径
    js_file_path = os.path.join('前端静态资源目录', 'js', 'ChangeLog.js')
    # 读取JavaScript代码文件
    with open(js_file_path, 'r', encoding='UTF-8') as f:
        f.readline()
        f.readline()
        原始文本 = f.readline()

    项目版本号 = 原始文本.split(':')[1]
    项目版本号 = eval(项目版本号.split(',')[0])

    return 项目版本号
