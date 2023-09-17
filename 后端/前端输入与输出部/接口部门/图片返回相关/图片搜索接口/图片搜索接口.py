from flask import Blueprint

from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器

search_bp = Blueprint('admin', __name__)


@search_bp.route('/Search/<tag>')
def Search(tag):
    压缩图片信息资源 = 图片信息资源管理器.搜索压缩图片信息资源(tag)
    # 把压缩图片信息资源中的元组数据类型全部换成列表
    压缩图片信息资源 = [list(i) for i in 压缩图片信息资源]
    print(f'压缩图片信息资源 {压缩图片信息资源}')
    return 压缩图片信息资源
