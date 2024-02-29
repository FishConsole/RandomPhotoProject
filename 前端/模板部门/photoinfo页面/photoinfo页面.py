import unittest

from flask import render_template, Blueprint, Flask

from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_前端 import info_调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

PhotoInfo_bp = Blueprint('PhotoInfo', __name__)


@PhotoInfo_bp.route('/PhotoInfo/<id>')
def PhotoInfo(id):
    # 从数据库中获得数据
    标签 = 图片信息资源管理器().获取指定_压缩_图片信息资源(id)[0][1]

    return render_template('PhotoInfo.html',
                           时间=标签[:10],
                           路径=id,
                           域名=路径控制.启动位置.域名(),
                           调试模式=info_调试模式())


class test_PhotoInfo(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(PhotoInfo_bp)
        self.app.template_folder = 路径控制.前端资源目录().模板资源目录()
        self.app.static_folder = 路径控制.前端资源目录().静态资源目录()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_Photo信息(self):
        响应 = self.client.get('/PhotoInfo/20240223155701.jpg')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容
