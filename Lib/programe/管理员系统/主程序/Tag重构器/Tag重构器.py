from flask import Blueprint, render_template, request

from Lib.programe.管理员系统.错误页面.错误页面 import 错误页面
from Lib.依赖.运维相关.调试模式 import 调试模式

admin_edittag_page_bp = Blueprint('admin_edittag_page', __name__)
admin_edittag_execute_photoinfo_upload_bp = Blueprint('admin_edittag_execute_photoinfo_upload', __name__)


@admin_edittag_page_bp.route('/admin~/<token>/edittag')
def edittag_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_edittag.html')


@admin_edittag_execute_photoinfo_upload_bp.route('/admin_thing~/edittag/')
def admin_edittag_execute_photoinfo_upload():
    图片名字=request.args.get('img_name')
    新的tag=request.args.get('content')
    pass

