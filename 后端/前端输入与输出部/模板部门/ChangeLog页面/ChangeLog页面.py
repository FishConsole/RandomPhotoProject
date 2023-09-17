from flask import render_template, Blueprint

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import ChangeLog_页面调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

ChangeLog_bp = Blueprint('ChangeLog', __name__)


@ChangeLog_bp.route('/ChangeLog')
def ChangeLog():
    return render_template('ChangeLog.html',
                           域名=路径控制.启动位置.域名(),
                           调试模式=ChangeLog_页面调试模式())
