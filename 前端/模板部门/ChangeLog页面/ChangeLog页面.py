import unittest

from flask import render_template, Blueprint, Flask
import os

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import ChangeLog_页面调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

ChangeLog_bp = Blueprint('ChangeLog', __name__)


@ChangeLog_bp.route('/ChangeLog')
def ChangeLog():
    return render_template('ChangeLog.html',
                           域名=路径控制.启动位置.域名(),
                           调试模式=ChangeLog_页面调试模式())


class test_ChangeLog(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(ChangeLog_bp)
        self.app.template_folder = 路径控制.前端资源目录().模板资源目录()
        self.app.static_folder = 路径控制.前端资源目录().静态资源目录()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_更新记录(self):
        响应 = self.client.get('/ChangeLog')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容
