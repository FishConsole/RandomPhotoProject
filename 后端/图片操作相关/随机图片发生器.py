import os
import random

from 后端.后端执行与回调部.回调相关.图片返回器 import 图片返回器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 随机图片发生器(model, 图片信息资源):
    if len(图片信息资源) == 0:
        return 图片返回器.随机选择的图片_失败()
    else:
        随机抽取 = random.sample(图片信息资源, 1)
        名字 = 随机抽取[0][0]
        图片 = os.path.join(路径控制().图片资源路径().主站图片资源路径().主站原始图片_路径(), 名字)
        # 如果使用原图，那么就会操作一次计数器
        # 否则就去读取压缩图片并且覆盖之前的
        CallStatistics目录 = os.path.join(路径控制.前端资源目录().CallStatistics(), "CallStatistics.txt")
        if model:
            with open(CallStatistics目录, 'r') as f:
                CallStatistics = f.read()
                if CallStatistics in '':
                    CallStatistics = 0
                f.close()
            CallStatistics = str(int(CallStatistics) + 1)
            with open(CallStatistics目录, 'w') as f:
                f.write(CallStatistics)
                f.close()
        else:
            图片 = os.path.join(路径控制.图片资源路径().主站图片资源路径().主站压缩图片_路径(), 名字)
        return 图片


def test随机图片发生器():
    print(随机图片发生器("电脑", [["1", "2", "3", "4"], ["1", "2", "3", "4"]]))
