import os

from flask import Blueprint, send_file

from 后端.后端执行与回调部.回调相关.图片返回器 import 图片返回器
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.杂项.文件读写器 import 文件读写器
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

Select_bp = Blueprint('Select', __name__)


@Select_bp.route('/Select/<filename>')
def Select_select(filename):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定_压缩_图片信息资源(filename)
    if 压缩图片信息资源 != []:
        if not 调试模式():
            上一次统计 = int(文件读写器('上一次统计.txt').读取())
            文件读写器('上一次统计.txt').写入(str(上一次统计 + 1))
        return send_file(os.path.join(路径控制.主站原始图片_路径(), filename))
    else:
        return 图片返回器.返回选择的图片_失败()


@Select_bp.route('/SelectNotCount/<filename>')
def Select_SelectNotCount(filename):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定_压缩_图片信息资源(filename)
    if 压缩图片信息资源 != []:
        return send_file(os.path.join(路径控制.主站原始图片_路径(), filename))
    else:
        return 图片返回器.返回选择的图片_失败()
