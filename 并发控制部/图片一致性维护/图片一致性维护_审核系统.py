import time

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.后端执行与回调部.执行部门.邮件相关.smtp_server import 发送邮件
from 后端.图片操作相关.图片路径提取 import 图片路径提取
from 后端.图片操作相关.审核系统 import 随机数发生器


def 图片一致性维护_审核队列_功能():
    审核队列_图片信息资源 = 图片路径提取(路径控制.图片资源路径().审核系统图片资源路径().审核系统原始图片_路径())
    if len(审核队列_图片信息资源) > 0:
        随机数发生器_生成的数字 = 随机数发生器(10)
        with open('shenhe_token', 'w') as f:
            f.write(随机数发生器_生成的数字)
            f.close()

        发送邮件(
            f"<h2>RandomPhoto上传中心</h2>有用户上传了图片，请尽快审核<br>（剩余图片数量{len(审核队列_图片信息资源)}）<br>这里是审核的网址：https://www.root-a.top/admin~/{随机数发生器_生成的数字}/main")


def 图片一致性维护_审核队列(测试状态=False):
    print(" * 审核图片一致性维护启动")
    while True:
        if 测试状态:
            图片一致性维护_审核队列_功能()
            break
        else:
            try:
                图片一致性维护_审核队列_功能()
            except:
                pass

        time.sleep(30 * 60)


def test图片一致性维护_审核队列():
    图片一致性维护_审核队列(True)
