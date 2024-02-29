import os
import time
from datetime import datetime

from flask import request, Blueprint

from 后端.后端执行与回调部.执行部门.邮件相关.smtp_server import 发送邮件

from 后端.后端执行与回调部.回调相关.文件上传器 import 文件上传器

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制

upload_bp = Blueprint('upload', __name__)


def 路径控制分部():
    return 路径控制.图片资源路径().审核系统图片资源路径().审核系统原始图片_路径()


def test路径控制_文件上传器分部():
    assert os.path.exists(路径控制分部()), True


@upload_bp.route('/UploadStart', methods=['POST'])
def upload_start():
    文件 = request.files.get('file')

    上传目录 = os.path.join(路径控制分部())
    允许的扩展名 = {'png', 'jpg', 'jpeg'}
    最大图片数量 = 200  # 最大允许上传的图片数量

    待审核文件集 = os.listdir(os.path.join(路径控制分部()))
    现在的图片数量 = len(待审核文件集)
    if 现在的图片数量 > 最大图片数量:
        try:
            发送邮件(f"RandomPhoto上传中心：审核队列已满，请立即处理")
        except:
            pass
        return 文件上传器.审核队列_满()

    def 是否为允许的文件类型(文件名):
        扩展名验证 = 文件名.split(".")[-1] in 允许的扩展名
        return 扩展名验证

    def 获取文件大小(文件名):
        文件名.seek(0, os.SEEK_END)
        文件大小 = 文件名.tell()
        文件名.seek(0)
        return 文件大小

    if 'file' not in request.files:
        return 文件上传器.没有文件部分()

    if 文件.filename == '':
        return 文件上传器.未选择文件()

    if not 是否为允许的文件类型(文件.filename):
        return 文件上传器.无效的文件类型()

    文件大小 = 获取文件大小(文件)
    最大文件大小 = 20 * 1024 * 1024  # 20MB
    if 文件大小 > 最大文件大小:
        return 文件上传器.文件大小限制(文件.filename)

    # 使用当前时间戳构造文件名
    time.sleep(0.001)
    时间戳 = datetime.now().strftime("%Y%m%d%H%M%S")
    文件扩展名 = 文件.filename.split(".")[-1]
    新文件名 = f"{时间戳}.jpg"
    文件路径 = os.path.join(上传目录, 新文件名)

    # 处理文件名冲突
    文件计数 = 1
    while os.path.exists(文件路径):
        # 若文件名已存在，通过增加计数来生成新的文件名
        新文件名 = f"{时间戳}_{文件计数}.jpg"
        文件路径 = os.path.join(上传目录, 新文件名)
        文件计数 += 1

    os.makedirs(上传目录, exist_ok=True)
    文件.save(文件路径)

    try:
        with open(路径控制.前端资源目录.shenhe_token(), 'r') as f:
            随机数发生器_生成的数字 = f.read()
            f.close()
            发送邮件(
                f"<h2>RandomPhoto上传中心</h2>有用户上传了图片，请尽快审核<br>）<br>这里是审核的网址：https://www.root-a.top/admin~/{随机数发生器_生成的数字}/main")
    except:
        pass

    return 文件上传器.文件上传成功(新文件名)
