from flask import Blueprint, render_template, request

from Lib.programe.管理员系统.错误页面.错误页面 import 错误页面
from Lib.依赖.数据库操作相关.审核系统图片标签重构编辑器 import 审核系统图片标签重构编辑器
from Lib.依赖.运维相关.调试模式 import 调试模式

admin_edittag_page_bp = Blueprint('admin_edittag_page', __name__)
admin_edittag_execute_photoinfo_upload_bp = Blueprint('admin_edittag_execute_photoinfo_upload', __name__)
admin_edittag_execute_photoinfo_next_bp = Blueprint('admin_edittag_execute_photoinfo_next', __name__)
admin_edittag_execute_photoinfo_cancel_bp = Blueprint('admin_edittag_execute_photoinfo_cancel', __name__)


@admin_edittag_page_bp.route('/admin~/<token>/edittag')
def edittag_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_edittag.html')


@admin_edittag_execute_photoinfo_upload_bp.route('/info_thing/Upload')
def admin_edittag_execute_photoinfo_upload():
    图片名字 = request.args.get('img_path')
    新的tag = request.args.get('content')
    result = 审核系统图片标签重构编辑器.提交请求(图片名字, 新的tag)
    return result


@admin_edittag_execute_photoinfo_next_bp.route('/info_thing/next')
def admin_edittag_execute_photoinfo_next():
    content = request.args.get('content')
    img_name = request.args.get('img_name')
    first = request.args.get('first')
    result = 审核系统图片标签重构编辑器.下一张图片(content, img_name, first)
    return result


@admin_edittag_execute_photoinfo_cancel_bp.route('/info_thing/cancel/<name>')
def admin_edittag_execute_photoinfo_cancel(name):
    result = 审核系统图片标签重构编辑器.取消更改(name)
    return result
