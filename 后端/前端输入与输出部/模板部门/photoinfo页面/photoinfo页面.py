import os

from flask import render_template, Blueprint

from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import info_调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

PhotoInfo_bp = Blueprint('PhotoInfo', __name__)


@PhotoInfo_bp.route('/PhotoInfo/<id>')
def PhotoInfo(id):
    # 从数据库中获得数据

    路径 = os.path.join(路径控制.主站原始图片_路径(), id)
    # 删除路径中可能会出现的斜线
    路径 = 路径.replace('/', '\\')
    # 内容 = 介绍
    # 标签 = Image_Location(os.path.join(路径控制.主站原始图片_路径(), id)).get_image_exif()['拍摄时间']

    标签 = 图片信息资源管理器.获取指定_压缩_图片信息资源(id)[0][1]

    return render_template('PhotoInfo.html',
                           时间=标签[:10],
                           路径=路径,
                           域名=路径控制.启动位置.域名(),
                           调试模式=info_调试模式())
