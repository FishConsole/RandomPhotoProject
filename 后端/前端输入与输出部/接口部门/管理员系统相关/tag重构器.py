from flask import Blueprint, request

from 后端.后端执行与回调部.执行部门.数据库操作相关.审核系统图片标签重构编辑器 import 审核系统图片标签重构编辑器

admin_edittag_execute_photoinfo_bp = Blueprint('admin_edittag_execute_photoinfo_upload', __name__)


@admin_edittag_execute_photoinfo_bp.route('/info_thing/Upload')
def admin_edittag_execute_photoinfo_upload():
    图片名字 = request.args.get('img_path')
    新的tag = request.args.get('content')
    新的tag = 新的tag[:500]
    result = 审核系统图片标签重构编辑器.提交请求(图片名字, 新的tag)
    return result


@admin_edittag_execute_photoinfo_bp.route('/info_thing/next')
def admin_edittag_execute_photoinfo_next():
    content = request.args.get('content')
    img_name = request.args.get('img_name')
    first = request.args.get('first')
    print(f'first:{first}')
    result = 审核系统图片标签重构编辑器.下一张图片(content, img_name, first)
    return result


@admin_edittag_execute_photoinfo_bp.route('/info_thing/cancel/<name>')
def admin_edittag_execute_photoinfo_cancel(name):
    result = 审核系统图片标签重构编辑器.取消更改(name)
    return result
