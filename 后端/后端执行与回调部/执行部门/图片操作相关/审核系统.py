import random
import shutil  # shutil模块提供了移动、复制、 压缩、解压等操作，恰好与os互补
import os
import jieba

from 后端.后端执行与回调部.回调相关.审核系统 import 图片审核
from 后端.后端执行与回调部.执行部门.图片操作相关.图片大小检测 import 图片大小检测
from 后端.后端执行与回调部.执行部门.图片操作相关.图片路径提取 import 图片路径提取
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 随机数发生器(length):
    hex_digits = "0123456789abcdef"
    return ''.join(random.choice(hex_digits) for _ in range(length))


def 删除审核图片(ImageName):
    # 删除指定路径的文件
    import os
    try:
        源路径 = os.path.join(路径控制.审核系统原始图片_路径(), ImageName)
        压缩路径 = os.path.join(路径控制.审核系统压缩图片_路径(), ImageName)

        os.remove(源路径)
        os.remove(压缩路径)
        return 图片审核.删除审核图片.删除审核图片_成功(ImageName)
    except OSError as 错误:
        return 图片审核.删除审核图片.删除审核图片_失败(ImageName, 错误)


def 通过审核图片(图片名字, 负载):
    try:
        jieba.load_userdict(os.path.join('后端', '后端执行与回调部', '执行部门', '图片操作相关', '分词包', 'dict.txt'))
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

        return 图片审核.通过审核图片.通过审核图片_成功(图片名字)

    except Exception as e:
        return 图片审核.通过审核图片.通过审核图片_失败(图片名字, e)


def 审核():
    审核队列_压缩图片信息资源 = 图片路径提取(路径控制.审核系统压缩图片_路径())
    return 审核队列_压缩图片信息资源
