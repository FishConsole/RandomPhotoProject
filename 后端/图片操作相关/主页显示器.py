from flask import render_template
import os

from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import *

CallStatistics路径 = os.path.join(路径控制.前端资源目录().CallStatistics(), 'CallStatistics.txt')


def home_(压缩图片信息资源):
    global CallStatistics路径
    with open(CallStatistics路径, 'r') as f:
        CallStatistics = f.read()
        if CallStatistics in '':
            CallStatistics = 0
        f.close()

    # 反转数组，这样可以让新上传的图片排在前面
    压缩图片信息资源 = 压缩图片信息资源[::-1]

    # 这种情况的出现可能是因为当天没有最新的图片，因此要随便整点东西出来
    if len(压缩图片信息资源) == 0:
        压缩图片信息资源 = 图片信息资源管理器().获取指定页数的压缩图片信息资源(1)

    # 把压缩图片信息资源中的元组数据类型全部换成列表
    压缩图片信息资源 = [list(i) for i in 压缩图片信息资源]
    return render_template('index.html', 统计调用次数=CallStatistics, Image_Count=len(压缩图片信息资源),
                           图片信息资源={"Image_Count": len(压缩图片信息资源),
                                         "Image_Data": 压缩图片信息资源},
                           下一页=2,
                           上一页=1,
                           强制返回='false',
                           域名=路径控制.启动位置.域名(),
                           调试模式=index页面_调试模式())



def home_page_(page, 压缩图片信息资源):
    global CallStatistics路径
    with open(CallStatistics路径, 'r') as f:
        CallStatistics = f.read()
        if CallStatistics in '':
            CallStatistics = 0
        f.close()

    try:
        page = int(page)
        # 检查page是否为1，如果为1则不能继续往下减
        if page == 1:
            上一页 = 1
        else:
            上一页 = page - 1

        # 检查下一页是否有内容，没有内容返回当页
        下一页 = page + 1
        强制返回器 = 'false'
        if len(压缩图片信息资源) == 0:
            下一页 = 下一页 - 2
            强制返回器 = 'true'

        # 把压缩图片信息资源中的元组数据类型全部换成列表
        压缩图片信息资源 = [list(i) for i in 压缩图片信息资源]
        return render_template('index.html', 统计调用次数=CallStatistics, Image_Count=len(压缩图片信息资源),
                               图片信息资源={"Image_Count": len(压缩图片信息资源),
                                             "Image_Data": 压缩图片信息资源},
                               下一页=下一页,
                               上一页=上一页,
                               强制返回=强制返回器,
                               域名=路径控制.启动位置.域名(),
                               调试模式=index页面_调试模式())
    except ValueError:
        return ''
