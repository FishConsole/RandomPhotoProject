import os
import time

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 显示LOG
from 后端.图片操作相关.图片压缩库 import ResizeImage
from 后端.图片操作相关.图片路径提取 import 图片路径提取
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 图片一致性维护_功能():
    图片信息资源 = 图片路径提取(路径控制.图片资源路径().主站图片资源路径().主站原始图片_路径())
    压缩图片信息资源 = 图片路径提取(路径控制.图片资源路径().主站图片资源路径().主站压缩图片_路径())

    for 图片名字 in 图片信息资源.keys():
        if not os.path.exists(os.path.join(路径控制.图片资源路径().主站图片资源路径().主站压缩图片_路径(), 图片名字)):
            print(f"图片一致性维护：生成主页缩略图 {图片名字}")
            文件输入 = os.path.join(路径控制.图片资源路径().主站图片资源路径().主站原始图片_路径(), 图片名字)
            文件输出 = os.path.join(路径控制.图片资源路径().主站图片资源路径().主站压缩图片_路径(), 图片名字)
            ResizeImage(文件输入, 文件输出)

    for 图片名字 in 压缩图片信息资源.keys():
        try:
            if not os.path.exists(os.path.join(路径控制.图片资源路径().主站图片资源路径().主站原始图片_路径(), 图片名字)):
                os.remove(os.path.join(路径控制.图片资源路径().主站图片资源路径().主站压缩图片_路径(), 图片名字))
                print(f"图片一致性维护：未发现对应的主站原始图片，删除主页缩略图 {图片名字}")
                图片信息资源管理器().删除压缩图片信息资源(图片名字)
        except FileNotFoundError as 错误信息:
            # 这种情况是数据库那边的问题，或者文件真的不存在
            print(f'图片一致性维护：出现异常 - 文件不存在 {错误信息}')
            pass


def 图片一致性维护(测试状态=False):
    import sys
    LOGS日志文件 = os.path.join(路径控制.日志目录().LOGS日志目录(), "图片一致性维护.txt")
    with open(LOGS日志文件, "w+", encoding='utf-8') as file:
        file.write("")
        file.close()
    with open(LOGS日志文件, 'a', encoding='utf-8') as file:
        if not 显示LOG():
            sys.stdout = file
        print(" * 业务图片一致性维护线程启动")
        while True:
            if 测试状态:
                图片一致性维护_功能()
                break
            else:
                try:
                    图片一致性维护_功能()
                except Exception as e:
                    print(f"图片一致性维护报错:{e}")
            time.sleep(5)


def test图片一致性维护():
    图片一致性维护(True)
