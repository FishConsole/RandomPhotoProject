# -*- coding: utf-8 -*-
import re
import os


def 版本号提取():
    # 读取JavaScript代码文件
    with open(os.path.join('static', 'js', 'ChangeLog.js'), 'r', encoding='UTF-8') as f:
        js_code = f.read()

    try:
        # 使用正则表达式匹配版本号
        pattern = r"'版本号':'(.*?)',"
        match = re.search(pattern, js_code)

        项目版本号 = match.group(1)
    except AttributeError:
        return 'ERROR! :未找到版本号'
    return 项目版本号

