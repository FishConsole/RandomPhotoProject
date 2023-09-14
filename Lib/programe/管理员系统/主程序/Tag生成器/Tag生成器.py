import os

from flask import Blueprint, render_template

from Lib.依赖.图片操作相关.自动图像标签生成器 import 二次元图片标签自动生成
from Lib.依赖.运维相关.调试模式.调试模式 import 调试模式
from Lib.programe.管理员系统.错误页面.错误页面 import 错误页面

admin_AutoTag_page_bp = Blueprint('admin_AutoTag_page', __name__)
admin_AutoTag_bp = Blueprint('admin_AutoTag', __name__)


@admin_AutoTag_page_bp.route('/admin~/<token>/autotag')
def admin_AutoTag_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_autotag.html')


@admin_AutoTag_bp.route('/admin_thing~/shenhe/AutoTag/<ImgName>')
def 自动标签生成器(ImgName):
    图片名称 = os.path.join('img', '审核系统原始图片', ImgName)
    try:
        return 二次元图片标签自动生成([图片名称])
    except OSError as e:
        return {'error': True, 'message': f'指定文件不存在 - {e}', 'result': {}}
