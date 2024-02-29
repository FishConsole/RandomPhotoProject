import os.path

from flask import Blueprint, render_template, send_file

from 前端.模板部门.管理员系统相关.错误页面 import 错误页面
from 后端.后端执行与回调部.回调相关.db转xlsx import 数据库转xlsx
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.图片操作相关.审核系统 import 审核

admin_page_bp = Blueprint('admin_page', __name__)


class 路径控制分部:
    @staticmethod
    def shenhe_token():
        return 路径控制.前端资源目录().shenhe_token()

    @staticmethod
    def 临时xlsx地址():
        return 路径控制.临时资源路径().临时excel路径()


@admin_page_bp.route('/admin~/<token>/main')
def admin(token):
    try:
        with open(路径控制分部.shenhe_token(), 'r') as f:
            文件_token = f.read().strip()
            if 文件_token != token and 调试模式() == False:
                return 错误页面()
    except FileNotFoundError:
        # 创建这个文件
        with open(路径控制分部.shenhe_token(), 'w') as f:
            f.write(token)
    return render_template('admin.html', token=token)


@admin_page_bp.route('/admin~/<token>/shenhe')
def admin_shenhe_page(token):
    with open(路径控制分部.shenhe_token(), 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_shenhe.html', 数据源=审核())


@admin_page_bp.route('/admin~/<token>/edittag')
def edittag_page(token):
    with open(路径控制分部.shenhe_token(), 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_edittag.html')


@admin_page_bp.route('/admin~/<token>/autotag')
def admin_AutoTag_page(token):
    with open(路径控制分部.shenhe_token(), 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_autotag.html')


@admin_page_bp.route('/admin~/<token>/OutputExcel')
def 导出数据库为excel(token):
    with open(路径控制分部.shenhe_token(), 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    数据库转xlsx().数据库转xlsx()
    return send_file(os.path.join(路径控制分部.临时xlsx地址(), 'output.xlsx'), as_attachment=True)
