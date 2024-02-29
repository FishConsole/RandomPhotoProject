from flask import make_response


@main.route('/sitemap.xml', methods=['GET'])
def sitemap():
    from 后端.后端执行与回调部.执行部门.运维相关.站点地图生成器 import 生成站点地图
    from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器

    生成的XML = 生成站点地图([
        {'图片信息资源': 图片信息资源管理器.站点地图生成器_获取全部图片信息(), '优先级': '0.5', '分类': 'info'},
    ])

    response = make_response(生成的XML)
    response.headers["Content-Type"] = "application/xml"

    return response
