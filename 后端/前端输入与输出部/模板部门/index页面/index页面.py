from flask import Blueprint
from 后端.后端执行与回调部.执行部门.图片操作相关.主页显示器 import home_, home_page_
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器

index_bp = Blueprint('index', __name__)


@index_bp.route('/index/', methods=['get'])
def 主页():
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获得最新上传的图片()
    print(f'压缩图片信息资源: {len(压缩图片信息资源)}')
    return home_(压缩图片信息资源=压缩图片信息资源)


@index_bp.route('/index/<page>', methods=['get'])
def 主页_子页(page):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定页数的压缩图片信息资源(page)
    print(压缩图片信息资源)
    return home_page_(page, 压缩图片信息资源)
