import os


def 后端启动器():
    from 后端.后端执行与回调部.执行部门.运维相关.所需库一键部署 import 所需库一键部署
    from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式_广播站 import 调试模式_广播站
    from 后端.后端执行与回调部.执行部门.运维相关.调试模式 import 调试模式
    from 后端.后端执行与回调部.执行部门.运维相关.版本号提取 import 版本号提取

    if not 调试模式.调试模式():
        print(f' * RandomPhoto_当前版本: {版本号提取()} - [业务模式]')
    else:
        print(f' * RandomPhoto_当前版本: {版本号提取()} - [调试模式]')
    print('-' * 90)
    调试模式_广播站()
    所需库一键部署()

    import threading
    from flask import Flask
    from flask_cors import CORS  # 跨域访问限制
    from flask_sslify import SSLify

    from 后端.前端输入与输出部.接口部门.图片返回相关.图片返回器 import img_bp
    from 后端.前端输入与输出部.接口部门.文件上传相关.文件上传器 import upload_bp
    from 后端.前端输入与输出部.接口部门.背景音乐相关.背景音乐 import 网易云爬虫_bp
    from 后端.前端输入与输出部.接口部门.管理员系统相关.Tag生成器 import admin_AutoTag_bp
    from 后端.前端输入与输出部.接口部门.管理员系统相关.图片审核系统 import admin_DeletePhoto_bp, admin_PassPhoto_bp
    from 后端.前端输入与输出部.接口部门.管理员系统相关.Tag重构器 import admin_edittag_execute_photoinfo_bp
    from 后端.前端输入与输出部.接口部门.图片返回相关.图片搜索接口.图片搜索接口 import search_bp
    from 后端.前端输入与输出部.接口部门.图片返回相关.指定图片接口.指定图片接口 import Select_bp
    from 后端.前端输入与输出部.接口部门.图片返回相关.随机图片接口.随机图片接口 import Random_bp

    from 后端.前端输入与输出部.模板部门.管理员系统相关.管理员系统 import admin_page_bp
    from 后端.前端输入与输出部.模板部门.index页面.index页面 import index_bp
    from 后端.前端输入与输出部.模板部门.photoinfo页面.photoinfo页面 import PhotoInfo_bp
    from 后端.前端输入与输出部.模板部门.根页面.根页面 import root_bp
    from 后端.前端输入与输出部.模板部门.upload页面.upload页面 import upload_page_bp
    from 后端.前端输入与输出部.模板部门.ChangeLog页面.ChangeLog页面 import ChangeLog_bp

    from 后端.并发控制部.图片一致性维护.图片一致性维护_审核系统 import 图片一致性维护_审核队列
    from 后端.并发控制部.审核系统缩略图生成器.审核系统缩略图生成器 import 审核系统缩略图生成器
    from 后端.并发控制部.图片一致性维护.图片一致性维护_业务环境 import 图片一致性维护

    from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
    from 后端.后端执行与回调部.执行部门.运维相关.万能测试接口 import universal_bp

    from 后端.三方隔离接口部.海纳专用.海纳 import ocss_page_bp

    from 后端.并发控制部.自动死亡线程.自动死亡线程 import 自动死亡线程

    main = Flask(__name__)
    sslify = SSLify(main)

    CORS(main, resources={r"/前端静态资源目录/*": {"origins": "https://www.root-a.top"}})

    main.register_blueprint(universal_bp)

    main.register_blueprint(网易云爬虫_bp)

    main.register_blueprint(img_bp)

    main.register_blueprint(upload_bp)
    main.register_blueprint(upload_page_bp)

    main.register_blueprint(Random_bp)
    main.register_blueprint(Select_bp)

    main.register_blueprint(search_bp)

    main.register_blueprint(index_bp)

    main.register_blueprint(PhotoInfo_bp)

    main.register_blueprint(admin_page_bp)
    main.register_blueprint(admin_DeletePhoto_bp)
    main.register_blueprint(admin_PassPhoto_bp)
    main.register_blueprint(admin_edittag_execute_photoinfo_bp)
    main.register_blueprint(admin_AutoTag_bp)

    main.register_blueprint(ocss_page_bp)

    main.register_blueprint(root_bp, name='root_bp')

    main.register_blueprint(ChangeLog_bp)

    ############################################################

    main.config['SSL_CERTIFICATE'] = 'ssl/root-a.top_bundle.crt'
    main.config['SSL_PRIVATE_KEY'] = 'ssl/root-a.top.key'

    main.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024
    main.template_folder = os.path.join('..', '..', '前端模板目录')
    main.static_folder = os.path.join('..', '..', '前端静态资源目录')

    main.config['上一次统计'] = {}
    threading.Thread(target=图片一致性维护_审核队列, daemon=True).start()
    threading.Thread(target=审核系统缩略图生成器, daemon=True).start()
    threading.Thread(target=自动死亡线程, daemon=True).start()
    threading.Thread(target=图片一致性维护, daemon=True).start()
    main.run(host=路径控制.启动位置.启动位置(), port=443, threaded=False,
             ssl_context=(main.config['SSL_CERTIFICATE'], main.config['SSL_PRIVATE_KEY']),
             )
