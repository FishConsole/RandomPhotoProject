# -*- coding: utf-8 -*-
import os
import platform
import sys
from Lib.programe.调试模式 import 调试模式

当前操作系统 = platform.system().split('_')[0]
当前PIP目录 = os.path.join(os.path.dirname(sys.executable), 'Scripts')
# 这样一段代码的用处是递归调用，确保所有的库都安装，否则不会执行主程序
需求库 = {
    'flask': 'flask',
    'flask_cors': 'flask_cors',
    'flask_sslify': 'flask_sslify',
    'jieba': 'jieba',
    'exifread': 'exifread',
    'requests': 'requests',
    # 'tensorflow': 'tensorflow',
    # 'deepdanbooru': 'deepdanbooru',
    'Pillow': 'PIL',
}
镜像 = '-i https://pypi.tuna.tsinghua.edu.cn/simple '

print(f' * 所需库一键部署: 开始，当前调用镜像: {镜像},如果你的服务器不在中国境内，请删除这段代码')

计数器 = 0


def 所需库一键部署():
    if not 调试模式():
        global 计数器
        for i in 需求库.keys():
            print('初始化: 所需库一键部署: 检查库：', i, '是否存在')
            try:
                __import__(需求库[i])
            except:
                if 计数器 != 10:
                    print('所需库一键部署: 缺少库：', i, '正在安装', 计数器)
                    if 当前操作系统 == 'Windows':
                        print(f'{os.path.join(当前PIP目录, "pip")} install {i} {镜像}')
                        os.system(f'{os.path.join(当前PIP目录, "pip")} install {i} {镜像}')
                    else:
                        os.system(f'{os.path.join(当前PIP目录, "pip3")} install {i} {镜像}')
                    计数器 += 1
                else:
                    print('所需库一键部署: 安装库：', i, '超过10次，跳过')
                    计数器 = 0
                    continue
                所需库一键部署()
    else:
        print(' * 所需库一键部署: 调试模式，跳过')
