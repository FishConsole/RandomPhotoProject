import os

from flask import Blueprint

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.图片操作相关.自动图像标签生成器 import 二次元图片标签自动生成

admin_AutoTag_bp = Blueprint('admin_AutoTag', __name__)


def 路径控制分部():
    return 路径控制.图片资源路径().审核系统图片资源路径().审核系统原始图片_路径()


def test路径控制_自动标签生成器分部():
    assert os.path.exists(路径控制分部()), True


@admin_AutoTag_bp.route('/admin_thing~/shenhe/AutoTag/<ImgName>')
def 自动标签生成器(ImgName):
    图片名称 = os.path.join(路径控制分部(), ImgName)
    try:
        return 二次元图片标签自动生成([图片名称])
    except OSError as e:
        return {'error': True, 'message': f'指定文件不存在 - {e}', 'result': {}}
