import os

from 后端.后端执行与回调部.执行部门.图片操作相关.图片压缩库 import ResizeImage
from 后端.后端执行与回调部.执行部门.图片操作相关.图片路径提取 import 图片路径提取
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 审核系统缩略图生成器():
    import time
    while True:
        a = None
        try:
            审核队列_图片信息资源 = 图片路径提取(路径控制.审核系统原始图片_路径())
            审核队列_压缩图片信息资源 = 图片路径提取(路径控制.审核系统压缩图片_路径())

            for a in 审核队列_图片信息资源.keys():
                if not os.path.exists(os.path.join(路径控制.审核系统压缩图片_路径(), a)):
                    print(f"审核系统缩略图生成器：生成审核缩略图 {a}")
                    filein = os.path.join(路径控制.审核系统原始图片_路径(), a)
                    fileout = os.path.join(路径控制.审核系统压缩图片_路径(), a)
                    ResizeImage(filein, fileout)

            for b in 审核队列_压缩图片信息资源.keys():
                if not os.path.exists(os.path.join(路径控制.审核系统原始图片_路径(), b)):
                    os.remove(os.path.join(路径控制.审核系统压缩图片_路径(), b))

        except:
            try:
                # 出现报错直接删除对应的图片
                os.remove(os.path.join(路径控制.审核系统原始图片_路径(), a))
            except Exception as e:
                print(f"审核系统缩略图生成器：报错：{e}")
        time.sleep(20)
