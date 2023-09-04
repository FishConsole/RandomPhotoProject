from flask import Blueprint, render_template

from Lib.依赖.运维相关.调试模式 import 调试模式
from Lib.programe.管理员系统.错误页面.错误页面 import 错误页面

admin_page_bp = Blueprint('admin_page', __name__)


@admin_page_bp.route('/admin~/<token>/main')
def admin(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin.html', token=token)
