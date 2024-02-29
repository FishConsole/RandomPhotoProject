import os
import random
import shutil  # shutil模块提供了移动、复制、 压缩、解压等操作，恰好与os互补

from 后端.后端执行与回调部.回调相关.审核系统 import 图片审核
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.图片操作相关.图片大小检测 import 图片大小检测
from 后端.图片操作相关.图片路径提取 import 图片路径提取


class 路径控制分部:
    @staticmethod
    def 审核系统压缩图片():
        return 路径控制.图片资源路径().审核系统图片资源路径().审核系统压缩图片_路径()

    @staticmethod
    def 审核系统原始图片():
        return 路径控制.图片资源路径().审核系统图片资源路径().审核系统原始图片_路径()

    @staticmethod
    def 主站原始图片():
        return 路径控制.图片资源路径().主站图片资源路径().主站原始图片_路径()


def test路径控制_管理员系统分部():
    assert os.path.exists(路径控制分部.审核系统原始图片())
    assert os.path.exists(路径控制分部.审核系统压缩图片())
    assert os.path.exists(路径控制分部.主站原始图片())


def 随机数发生器(length):
    hex_digits = "0123456789abcdef"
    return ''.join(random.choice(hex_digits) for _ in range(length))


def 删除审核图片(ImageName):
    # 删除指定路径的文件
    import os
    try:
        源路径 = os.path.join(路径控制分部.审核系统原始图片(), ImageName)
        压缩路径 = os.path.join(路径控制分部.审核系统压缩图片(), ImageName)

        os.remove(源路径)
        os.remove(压缩路径)
        return 图片审核.删除审核图片.删除审核图片_成功(ImageName)
    except OSError as 错误:
        return 图片审核.删除审核图片.删除审核图片_失败(ImageName, 错误)


def 通过审核图片(图片名字, 标签):
    try:
        源路径 = os.path.join(路径控制分部.审核系统原始图片(), 图片名字)
        压缩路径 = os.path.join(路径控制分部.审核系统压缩图片(), 图片名字)
        目标路径 = os.path.join(路径控制分部.主站原始图片(), 图片名字)

        图片信息资源管理器().写入压缩图片信息资源(图片名字,
                                        图片大小检测(os.path.join(路径控制分部.审核系统压缩图片(), 图片名字)),
                                                标签)

        shutil.move(源路径, 目标路径)
        os.remove(压缩路径)

        return 图片审核.通过审核图片.通过审核图片_成功(str(图片名字))

    except Exception as e:
        return 图片审核.通过审核图片.通过审核图片_失败(str(图片名字), e)


def 审核():
    审核队列_压缩图片信息资源 = 图片路径提取(路径控制分部.审核系统压缩图片())
    return 审核队列_压缩图片信息资源
