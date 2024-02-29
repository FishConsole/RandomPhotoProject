import os
import time
import unittest
from urllib.parse import urlparse  # 获取链接中域名的一个库

from flask import Blueprint, send_file, request, Flask

from 后端.三方隔离接口部.海纳专用.密码工具 import 密码工具
from 后端.后端执行与回调部.执行部门.运维相关 import 路径控制
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 调试模式
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

img_bp = Blueprint('img', __name__)


##########################################
# 站点基本图片显示，给前端使用的
@img_bp.route('/img/<module>/<filename>', methods=['get'])
def img(filename, module):
    # model的意思是模式，这里的意思就是说：这里有五个路径，因此有五个model
    # filename的意思是文件名，这里的意思就是说：指定的路径名
    认可的来源 = ['www.root-a.top', 'root-a.top', '[::1]', '']
    本次来源 = request.headers.get('Referer')
    本次来源 = urlparse(本次来源).netloc

    # 开发阶段使用
    if 调试模式():
        本次来源 = 'www.root-a.top'
    print(f"来源  {本次来源}")
    海纳验证 = request.args.get('token')
    if 海纳验证 is not None:
        海纳验证 = 海纳验证.replace(' ', '+')
        解密内容 = 密码工具().解密(海纳验证)
        if 解密内容 == '解密失败':
            return send_file(os.path.join(路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))
        else:
            # 如果现在的时间减去解密得到的时间大于15，那么就是超时了
            if int(time.time()) - int(解密内容) > 60 * 1000:
                try:
                    return send_file(os.path.join(路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))
                except Exception as e:
                    print(e)
                    return send_file(
                        os.path.join('..', 路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))

            else:
                os.system('cls')
    else:
        if 本次来源 not in 认可的来源:
            return send_file(os.path.join(路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))

    if module == '主站原始图片':
        try:
            return send_file(
                str(os.path.join('..', 路径控制.图片资源路径().主站图片资源路径().主站原始图片_路径(), filename)))
        except Exception as e:
            print(e)
            return send_file(os.path.join('..', 路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))

    elif module == '主站压缩图片':
        try:
            return send_file(
                os.path.join('..', 路径控制.图片资源路径().主站图片资源路径().主站压缩图片_路径(), filename))
        except Exception as e:
            print(e)
            return send_file(os.path.join('..', 路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))

    elif module == '审核系统原始图片':
        try:
            return send_file(
                os.path.join('..', 路径控制.图片资源路径().审核系统图片资源路径().审核系统原始图片_路径(), filename))
        except Exception as e:
            print(e)
            return send_file(os.path.join('..', 路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))
    elif module == '审核系统压缩图片':
        try:
            return send_file(
                os.path.join('..', 路径控制.图片资源路径().审核系统图片资源路径().审核系统压缩图片_路径(), filename))
        except Exception as e:
            print(e)
            return send_file(os.path.join('..', 路径控制.反跨源回调图片().反跨源回调图片_路径(), "fankuayuan.png"))
    else:
        raise 404


########################################################################################

class test图片返回器(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(img_bp)
        self.app.template_folder = 路径控制.前端资源目录().模板资源目录()
        self.app.static_folder = 路径控制.前端资源目录().静态资源目录()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_img_主站原始图片(self):
        响应 = self.client.get('/img/主站原始图片/20231221134037.jpg')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容

    def test_img_主站压缩图片(self):
        响应 = self.client.get('/img/主站压缩图片/20231221134037.jpg')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容

    def test_img_审核系统原始图片(self):
        响应 = self.client.get('/img/审核系统原始图片/20231221134037.jpg')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容

    def test_img_审核系统压缩图片(self):
        响应 = self.client.get('/img/审核系统压缩图片/20231221134037.jpg')
        self.assertEqual(响应.status_code, 200)  # 假设成功时返回HTTP 200
        # 根据需要添加更多的断言，基于响应内容
