from flask import render_template, Blueprint
import os

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import upload_调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

upload_page_bp = Blueprint('upload_page', __name__)


@upload_page_bp.route('/Upload')
def 文件上传中心():
    return render_template('upload.html',
                           域名=路径控制.启动位置.域名(),
                           调试模式=upload_调试模式())
