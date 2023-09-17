import os
import sqlite3

from flask import Blueprint, jsonify

from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器

ocss_page_bp = Blueprint('index_page', __name__)


@ocss_page_bp.route('/affiliate/ocss/<page>', methods=['post', 'get'])
def ocss_page(page):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定页数的压缩图片信息资源(page)
    # 转换成可以识别的数据类型
    page = int(page)
    # 检查下一页是否有内容，没有内容返回当页
    # 分割后的压缩图片信息资源 = 压缩图片信息资源[(page - 1) * 12:(page + page) * 6]
    # 压缩图片信息资源是一个嵌套列表，第一个是图片名字，第二个是图片的规格，我们只要第一个就行了
    压缩图片信息资源 = [i[0] for i in 压缩图片信息资源]
    # 分割后的压缩图片信息资源 = 压缩图片信息资源[(page - 1) * 12:(page + page) * 6]

    conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
    # 创建游标对象
    cur = conn.cursor()
    # 创建表
    cur.execute(f"SELECT 路径 FROM 压缩图片信息资源")
    row = cur.fetchall()
    # 关闭连接
    conn.close()

    if len(压缩图片信息资源) == 0:
        等待回调的数据 = {"count": len(row), 'condition': False, "data": []}
        return jsonify(等待回调的数据)
    else:
        等待回调的数据 = {"count": len(row), 'condition': True, "data": 压缩图片信息资源}
        return jsonify(等待回调的数据)
