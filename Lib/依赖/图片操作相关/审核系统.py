import random
import shutil  # shutil模块提供了移动、复制、 压缩、解压等操作，恰好与os互补
import time

import jieba

from Lib.依赖.邮件相关.smtp_server import 发送邮件

from Lib.依赖.回调相关.回调中心 import 回调中心

from Lib.依赖.图片操作相关.图片压缩库 import ResizeImage
from Lib.依赖.图片操作相关.图片路径提取 import 图片路径提取
from Lib.依赖.图片操作相关.图片大小检测 import 图片大小检测

from Lib.依赖.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from Lib.依赖.运维相关.路径控制 import *


def 随机数发生器(length):
    hex_digits = "0123456789abcdef"
    return ''.join(random.choice(hex_digits) for _ in range(length))


def 审核队列_重新读取():
    while True:
        try:
            审核队列_图片信息资源 = 图片路径提取(路径控制.审核系统原始图片_路径())
            if len(审核队列_图片信息资源) > 0:
                随机数发生器_生成的数字 = 随机数发生器(10)
                with open('shenhe_token', 'w') as f:
                    f.write(随机数发生器_生成的数字)
                    f.close()

                发送邮件(
                    f"<h2>RandomPhoto上传中心</h2>有用户上传了图片，请尽快审核<br>（剩余图片数量{len(审核队列_图片信息资源)}）<br>这里是审核的网址：https://www.root-a.top/admin~/{随机数发生器_生成的数字}/main")
        except:
            pass
        time.sleep(30 * 60)


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


def 删除审核图片(ImageName):
    # 删除指定路径的文件
    import os
    try:
        源路径 = os.path.join(路径控制.审核系统原始图片_路径(), ImageName)
        压缩路径 = os.path.join(路径控制.审核系统压缩图片_路径(), ImageName)

        os.remove(源路径)
        os.remove(压缩路径)
        return 回调中心.审核系统.删除审核图片.删除审核图片_成功(ImageName)
    except OSError as 错误:
        return 回调中心.审核系统.删除审核图片.删除审核图片_失败(ImageName, 错误)


def 通过审核图片(图片名字, 负载):
    try:
        jieba.load_userdict(os.path.join('Lib','programe', '../../programe/分词包', 'dict.txt'))
        初始标签集合 = list(jieba.cut(负载))
        # 去掉长度为1的内容
        标签集合 = [x for x in 初始标签集合 if len(x) > 1]
        # 转换成字符串
        标签集合 = ''.join(标签集合)
        源路径 = os.path.join(路径控制.审核系统原始图片_路径(), 图片名字)
        压缩路径 = os.path.join(路径控制.审核系统压缩图片_路径(), 图片名字)
        目标路径 = os.path.join(路径控制.主站原始图片_路径(), 图片名字)

        图片信息资源管理器.写入压缩图片信息资源(图片名字,
                                                图片大小检测(os.path.join(路径控制.审核系统压缩图片_路径(), 图片名字)),
                                                标签集合)

        shutil.move(源路径, 目标路径)
        os.remove(压缩路径)

        return 回调中心.审核系统.通过审核图片.通过审核图片_成功(图片名字)

    except Exception as e:
        return 回调中心.审核系统.通过审核图片.通过审核图片_失败(图片名字, e)


def 审核():
    审核队列_压缩图片信息资源 = 图片路径提取(路径控制.审核系统压缩图片_路径())
    return 审核队列_压缩图片信息资源


