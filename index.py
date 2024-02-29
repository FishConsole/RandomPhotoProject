# -*- coding: utf-8 -*-
import threading

from 后端.后端启动器.后端启动器 import *
from 后端.测试部门.test_测试部门 import test测试部门总部
from 并发控制部.图片一致性维护.图片一致性维护_业务环境 import 图片一致性维护
from 并发控制部.图片一致性维护.图片一致性维护_审核系统 import 图片一致性维护_审核队列
from 并发控制部.审核系统缩略图生成器.审核系统缩略图生成器 import 审核系统缩略图生成器
from 并发控制部.自动死亡线程.自动死亡线程 import 自动死亡线程


def start_flask_server():
    test测试部门总部()
    print("-" * 90)
    threading.Thread(target=审核系统缩略图生成器).start()
    threading.Thread(target=自动死亡线程).start()
    threading.Thread(target=图片一致性维护).start()
    threading.Thread(target=图片一致性维护_审核队列).start()
    threading.Thread(target=后端启动器).start()


if __name__ == '__main__':
    start_flask_server()
