# -*- coding: utf-8 -*-
import os
import platform

当前操作系统 = platform.system().split('_')[0]

# 这样一段代码的用处是递归调用，确保所有的库都安装，否则不会执行主程序
# 还要装一个库Pillow
需求库 = ['flask', 'flask_cors', 'flask_sslify', 'jieba', 'exifread', 'requests', 'deepdanbooru']
镜像 = 'https://pypi.tuna.tsinghua.edu.cn/simple '

print(f' * 所需库一键部署: 开始，当前调用镜像: {镜像}')

计数器 = 0


def 所需库一键部署():
    global 计数器
    for i in 需求库:
        try:
            __import__(i)
        except:
            if 计数器 != 4:
                print('所需库一键部署: 缺少库：', i, '正在安装', 计数器)
                if 当前操作系统 == 'Windows':
                    os.system(f'pip install {i} -i {镜像}')
                else:
                    os.system(f'pip3 install {i}  -i {镜像}')
                计数器 += 1
            else:
                print('所需库一键部署: 安装库：', i, '超过10次，跳过')
                continue

            所需库一键部署()


所需库一键部署()
