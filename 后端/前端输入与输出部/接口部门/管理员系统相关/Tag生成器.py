import os

from flask import Blueprint

from 后端.后端执行与回调部.执行部门.图片操作相关.自动图像标签生成器 import 二次元图片标签自动生成

admin_AutoTag_bp = Blueprint('admin_AutoTag', __name__)


@admin_AutoTag_bp.route('/admin_thing~/shenhe/AutoTag/<ImgName>')
def 自动标签生成器(ImgName):
    图片名称 = os.path.join('img', '审核系统原始图片', ImgName)
    try:
        return 二次元图片标签自动生成([图片名称])
    except OSError as e:
        return {'error': True, 'message': f'指定文件不存在 - {e}', 'result': {}}
