import os
from datetime import time

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.后端执行与回调部.执行部门.邮件相关.smtp_server import 发送邮件


def 自动死亡线程():
    # 自动死亡机制的意思就是自己访问自己
    # 当然是访问存活报告，如果访问不了那么就说明自己在外网上已经死了
    # 那么就自觉的退出，让系统重启自己
    import requests
    from 后端.后端执行与回调部.执行部门.运维相关.调试模式 import 调试模式
    print(' * 自动死亡线程：自动死亡线程启动')
    if not 调试模式:
        while True:
            try:
                requests.get('https://root-a.top/survive')
            except:
                print(' * 自动死亡线程：自动死亡机制启动,程序关闭，等待服务端重启')
                # 官方库的重启函数
                if not 调试模式:
                    发送邮件('RandomPhoto主程序：服务器准备重启')
                os.system("sh 重启.sh")
                os._exit(0)
            time.sleep(60 * 2)
    else:
        print(' * 自动死亡线程：调试模式启动，线程退出')
