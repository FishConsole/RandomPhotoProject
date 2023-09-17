from flask import Blueprint, render_template

from 后端.后端执行与回调部.执行部门.图片操作相关.审核系统 import 审核
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 调试模式
from 后端.前端输入与输出部.模板部门.管理员系统相关.错误页面 import 错误页面

admin_page_bp = Blueprint('admin_page', __name__)


@admin_page_bp.route('/admin~/<token>/main')
def admin(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin.html', token=token)


@admin_page_bp.route('/admin~/<token>/shenhe')
def admin_shenhe_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_shenhe.html', 数据源=审核())


@admin_page_bp.route('/admin~/<token>/edittag')
def edittag_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_edittag.html')


@admin_page_bp.route('/admin~/<token>/autotag')
def admin_AutoTag_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_autotag.html')
