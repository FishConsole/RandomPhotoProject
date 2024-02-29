from flask import Blueprint, jsonify

from 后端.后端执行与回调部.回调相关.背景音乐 import bgm池
from 后端.后端执行与回调部.执行部门.运维相关.缓存相关.配置文件管理器 import 配置文件管理器
from 后端.后端执行与回调部.执行部门.爬虫.网易云爬虫.网易云爬虫 import 网易云爬虫_本地音乐提供器

网易云爬虫_bp = Blueprint('网易云爬虫', __name__)


@网易云爬虫_bp.route('/music', methods=['get'])
def 网易云爬虫():
    # 缓存对象 = 配置文件管理器('爬虫')
    # if not 缓存对象.读取文件('网易云爬虫_启动状态'):
    #     提取 = 网易云爬虫_本地音乐提供器()
    #     缓存对象 = 配置文件管理器('爬虫')
    #     缓存对象.插入文件({'网易云爬虫_启动状态': True})
    #     print('提取2', 提取)
    #     回调 = bgm池.网易云爬虫_成功(提取)
    #     缓存对象.插入文件({'网易云爬虫_启动状态': False})
    #     print('回调', 回调)
    #     return 回调
    # else:
    #     return jsonify({'状态': '正在爬取'})
    return ''
