import os
import unittest

from flask import Blueprint, send_file, Flask

from 后端.后端执行与回调部.回调相关.图片返回器 import 图片返回器
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

Select_bp = Blueprint('Select', __name__)


@Select_bp.route('/Select/<filename>')
def 指定图片接口(filename):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器().获取指定_压缩_图片信息资源(filename)
    if 压缩图片信息资源:
        return send_file(os.path.join(路径控制.图片资源路径().主站图片资源路径().主站原始图片_路径(), filename))
    else:
        return 图片返回器.返回选择的图片_失败()
