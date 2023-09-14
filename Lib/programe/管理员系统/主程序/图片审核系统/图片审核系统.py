from flask import Blueprint, render_template

from Lib.依赖.图片操作相关.审核系统 import 审核, 通过审核图片, 删除审核图片
from Lib.依赖.运维相关.调试模式.调试模式 import 调试模式

from Lib.programe.管理员系统.错误页面.错误页面 import 错误页面

admin_shenhe_page_bp = Blueprint('admin_shenhe_page', __name__)
admin_PassPhoto_bp = Blueprint('admin_PassPhoto', __name__)
admin_DeletePhoto_bp = Blueprint('admin_DeletePhoto', __name__)


@admin_shenhe_page_bp.route('/admin~/<token>/shenhe')
def admin_shenhe_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_shenhe.html', 数据源=审核())

@admin_PassPhoto_bp.route('/admin_thing~/shenhe/Accept/<tag>/<ImgName>')
def 通过审核图片_(ImgName, tag):
    # 获取前端传过来的负载json
    print(tag)
    return 通过审核图片(ImgName, tag)


@admin_DeletePhoto_bp.route('/admin_thing~/shenhe/Delete/<ImgName>')
def 删除审核图片_(ImgName):
    return 删除审核图片(ImgName)
