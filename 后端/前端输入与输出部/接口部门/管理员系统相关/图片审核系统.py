from flask import Blueprint

from 后端.后端执行与回调部.执行部门.图片操作相关.审核系统 import 通过审核图片, 删除审核图片

admin_PassPhoto_bp = Blueprint('admin_PassPhoto', __name__)
admin_DeletePhoto_bp = Blueprint('admin_DeletePhoto', __name__)


@admin_PassPhoto_bp.route('/admin_thing~/shenhe/Accept/<tag>/<ImgName>')
def 通过审核图片_(ImgName, tag):
    # 获取前端传过来的负载json
    print(tag)
    return 通过审核图片(ImgName, tag)


@admin_DeletePhoto_bp.route('/admin_thing~/shenhe/Delete/<ImgName>')
def 删除审核图片_(ImgName):
    return 删除审核图片(ImgName)
