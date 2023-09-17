import os
import random

from 后端.后端执行与回调部.回调相关.图片返回器 import 图片返回器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

def 随机图片发生器(model, 图片信息资源):
    if len(图片信息资源) == 0:
        return 图片返回器.随机选择的图片_失败()
    else:
        随机抽取 = random.sample(图片信息资源, 1)
        print(随机抽取)

        名字 = 随机抽取[0][0]
        图片 = os.path.join(路径控制.主站原始图片_路径(), 名字)

        # 如果使用原图，那么就会操作一次计数器
        # 否则就去读取压缩图片并且覆盖之前的
        if model:
            with open('上一次统计.txt', 'r') as f:
                上一次统计 = f.read()
                if 上一次统计 in '':
                    上一次统计 = 0
                f.close()
            上一次统计 = str(int(上一次统计) + 1)
            with open('上一次统计.txt', 'w') as f:
                f.write(上一次统计)
                f.close()
        else:
            图片 = os.path.join(路径控制.主站压缩图片_路径(), 名字)
        return 图片
