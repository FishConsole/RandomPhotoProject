# -*- coding: utf-8 -*-
import os
import platform
import sys

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import *

当前操作系统 = platform.system().split('_')[0]
当前PIP目录 = os.path.join(os.path.dirname(sys.executable), 'Scripts')
# 获取Python版本号
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

# 这样一段代码的用处是递归调用，确保所有的库都安装，否则不会执行主程序
需求库 = {
    'flask': 'flask',
    'flask_cors': 'flask_cors',
    'flask_sslify': 'flask_sslify',
    'jieba': 'jieba',
    'exifread': 'exifread',
    'requests': 'requests',
    'Pillow': 'PIL',
    'selenium': 'selenium',
    # 'tensorflow': 'tensorflow',
    # 'deepdanbooru': 'deepdanbooru',
}

if 调试模式_国内模式():
    镜像 = ' -i https://pypi.tuna.tsinghua.edu.cn/simple'
else:
    镜像 = ''

print(f' * 所需库一键部署: 开始，当前调用镜像: {镜像},如果你的服务器不在中国境内，请删除这段代码')
print(
    f' * 所需库一键部署 - 检查 - 当前操作系统：{当前操作系统} | PIP：目录{os.path.dirname(当前PIP目录)} | Python版本号为：{python_version}')
计数器 = 0

安装验证 = {}
for i in 需求库.keys():
    安装验证[i] = False


def 所需库一键部署():
    global 计数器, 安装验证
    if not 调试模式():
        print('-' * 90)
        for i in 需求库.keys():
            if not 安装验证[i]:
                # print(f'安装验证: {安装验证}')
                print('初始化: 所需库一键部署: 检查库：', i, '是否存在')
                try:
                    __import__(需求库[i])
                    安装验证[i] = True
                    计数器 = 0
                except:
                    if 计数器 != 10:
                        print('所需库一键部署: 缺少库：', i, '正在安装', 计数器)
                        if 当前操作系统 == 'Windows':
                            print(f'{os.path.join(当前PIP目录, "pip")} install  {镜像} {i}')
                            os.system(f'{os.path.join(当前PIP目录, "pip")} install  {镜像} {i}')
                        else:
                            os.system(f'pip{python_version} install  {镜像} {i}')
                        计数器 += 1
                    else:
                        print('所需库一键部署: 安装库：', i, '超过10次，跳过')
                        raise ValueError(
                            f"所需库一键部署: 网络故障或目标安装包：'{i}' 不存在，请前往 'Lib/所需库一键部署.py' 修复此问题")
                    所需库一键部署()
    else:
        print(' * 所需库一键部署: 调试模式，跳过')
