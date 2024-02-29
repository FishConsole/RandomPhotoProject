import unittest
from flask import Blueprint, Flask
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.图片操作相关.主页显示器 import home_, home_page_
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

index_bp = Blueprint('index', __name__)


@index_bp.route('/index/', methods=['get'])
def 主页():
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器().获得最新上传的图片()
    print(f'压缩图片信息资源: {len(压缩图片信息资源)}')
    return home_(压缩图片信息资源=压缩图片信息资源)


@index_bp.route('/index/<page>', methods=['get'])
def 主页_子页(page):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器().获取指定页数的压缩图片信息资源(page)
    print(压缩图片信息资源)
    return home_page_(page, 压缩图片信息资源)


class test_index页面(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(index_bp)
        self.app.template_folder = 路径控制.前端资源目录().模板资源目录()
        self.app.static_folder = 路径控制.前端资源目录().静态资源目录()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test默认主页(self):
        响应 = self.client.get('/index/')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200

    def test有翻页状态的主页(self):
        响应 = self.client.get('/index/1')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容
