from flask import Blueprint, send_file, request

from 后端.后端执行与回调部.执行部门.图片操作相关.随机图片发生器 import 随机图片发生器
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.杂项.文件读写器 import 文件读写器
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 调试模式

Random_bp = Blueprint('随机图片接口', __name__)


@Random_bp.route('/Random', methods=['get'])
def Random_Random():
    # 判断用户ua，根据用户的ua来选择需要返回的图片

    ua = request.headers.get('User-Agent')
    # 如果是windows或者mac
    if 'Windows' in ua or 'Macintosh' in ua:
        return Random_More_Random('横屏')

    # 如果是安卓
    elif 'Android' in ua:
        if 'Tablet' in ua:
            return Random_More_Random('平板')
        else:
            return Random_More_Random('竖屏')

    # 如果是鸿蒙
    elif 'Harmony' in ua:
        if 'Tablet' in ua:
            return Random_More_Random('平板')
        else:
            return Random_More_Random('竖屏')

    # 如果是ios
    elif 'iPhone' in ua or 'iPad' in ua:
        if 'Tablet' in ua:
            return Random_More_Random('平板')
        else:
            return Random_More_Random('竖屏')


@Random_bp.route('/Random/<model>', methods=['get'])
def Random_More_Random(model):
    """
    :param model: model的意思是：强制判断请求所需要的图片，有两种选项，分别返回不同的图片
    :return:
    """
    范围 = request.args.get('range')
    print(范围)
    # 从数据库中获得数据,要原图
    图片 = 随机图片发生器(True, 图片信息资源管理器.获取指定_版式_压缩图片信息资源(model, 范围))
    if not 调试模式():
        上一次统计 = int(文件读写器('上一次统计.txt').读取())
        文件读写器('上一次统计.txt').写入(str(上一次统计 + 1))

    return send_file(图片, mimetype='image/jpg')

@Random_bp.route('/RandomNotCount/')
def Random_RandomNotCount():
    # 判断用户ua，根据用户的ua来选择需要返回的图片

    ua = request.headers.get('User-Agent')
    # 如果是windows或者mac
    if 'Windows' in ua or 'Macintosh' in ua:
        return Random_More_RandomNotCount('横屏')

    # 如果是安卓
    elif 'Android' in ua:
        if 'Tablet' in ua:
            return Random_More_RandomNotCount('平板')
        else:
            return Random_More_RandomNotCount('竖屏')

    # 如果是鸿蒙
    elif 'Harmony' in ua:
        if 'Tablet' in ua:
            return Random_More_RandomNotCount('平板')
        else:
            return Random_More_RandomNotCount('竖屏')

    # 如果是ios
    elif 'iPhone' in ua or 'iPad' in ua:
        if 'Tablet' in ua:
            return Random_More_RandomNotCount('平板')
        else:
            return Random_More_RandomNotCount('竖屏')


@Random_bp.route('/RandomNotCount/<model>')
def Random_More_RandomNotCount(model):
    # 从数据库中获得数据
    if model == '横屏':
        图片 = 随机图片发生器(False, 图片信息资源管理器.获取指定_版式_压缩图片信息资源('横屏'))
        return send_file(图片, mimetype='image/jpg')
    elif model == '竖屏':
        图片 = 随机图片发生器(False, 图片信息资源管理器.获取指定_版式_压缩图片信息资源('竖屏'))
        return send_file(图片, mimetype='image/jpg')
