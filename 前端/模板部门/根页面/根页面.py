import unittest

from flask import Blueprint, render_template, Flask

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import main_调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

root_bp = Blueprint('root_bp', __name__)
模板资源动态绝对根路径 = 路径控制.前端资源目录().模板资源目录()


@root_bp.route('/')
def zhuye():
    return render_template('main.html',
                           域名=路径控制.启动位置.域名(),
                           调试模式=main_调试模式())


class test_index(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(root_bp)
        self.app.template_folder = 路径控制.前端资源目录().模板资源目录()
        self.app.static_folder = 路径控制.前端资源目录().静态资源目录()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_主页(self):
        响应 = self.client.get('/')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容
