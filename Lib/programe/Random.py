import os
import random

from Lib.路径控制 import 路径控制
from Lib.回调中心 import 回调中心


def Random(model, 图片信息资源):
    if len(图片信息资源) == 0:
        return 回调中心.图片返回器.随机选择的图片_失败()
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
