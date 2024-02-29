import unittest

from flask import Blueprint, Flask

from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

search_bp = Blueprint('admin', __name__)


def 相关度排序(标签数据集, 输入):
    result = {}
    a = 输入

    for i in 标签数据集:
        c = 0
        for ii in i[1]:
            if ii in a:
                c += 1
        if c in result:
            result[c].append(i)
        else:
            result[c] = [i]
    # print(result)
    a = result.keys()
    a = sorted(a, reverse=True)
    result2 = []
    for i in a:
        for ii in result[i]:
            result2.append(ii)

    return result2


@search_bp.route('/Search/<tag>')
def Search(tag):
    压缩图片信息资源 = 图片信息资源管理器().搜索压缩图片信息资源(tag)
    # 把压缩图片信息资源中的元组数据类型全部换成列表
    压缩图片信息资源 = [list(i) for i in 压缩图片信息资源]
    压缩图片信息资源 = 相关度排序(压缩图片信息资源, tag)
    return 压缩图片信息资源


class test_Search(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(search_bp)
        self.app.template_folder = 路径控制.前端资源目录().模板资源目录()
        self.app.static_folder = 路径控制.前端资源目录().静态资源目录()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_搜索接口(self):
        响应 = self.client.get('/Search/测试')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容
