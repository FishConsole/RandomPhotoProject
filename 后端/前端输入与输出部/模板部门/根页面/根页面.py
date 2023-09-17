from flask import Blueprint, render_template

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import main_调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

root_bp = Blueprint('index', __name__)


@root_bp.route('/')
def zhuye():
    return render_template('main.html',
                           域名=路径控制.启动位置.域名(),
                           调试模式=main_调试模式())
