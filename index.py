# -*- coding: utf-8 -*-

from Lib.所需库一键部署 import 所需库一键部署

所需库一键部署()

from Lib.版本号提取 import 版本号提取

print(f' * RandomPhoto_当前版本: {版本号提取()}')
print('-' * 90)

import threading

from flask import Flask, make_response
from flask_cors import CORS, cross_origin  # 跨域访问限制
from flask_sslify import SSLify

from Lib.programe.admin import *
from Lib.programe.图片返回器 import *
from Lib.programe.审核系统 import 审核队列_重新读取, 审核系统缩略图生成器
from Lib.programe.文件上传器 import upload_bp
from Lib.programe.调试模式 import 调试模式
from Lib.programe.重新读取 import 重新读取_
from Lib.smtp_server import 发送邮件
from Lib.路径控制 import 路径控制

from Lib.affiliate.海纳 import ocss_page_bp

main = Flask(__name__)
sslify = SSLify(main)

CORS(main, resources={r"/static/*": {"origins": "https://www.root-a.top"}})

main.register_blueprint(img_bp, name='img')

main.register_blueprint(upload_bp, name='upload')

main.register_blueprint(Random_bp)
main.register_blueprint(Random_More_bp, name='Random_More')
main.register_blueprint(Random_NotCount_bp, name='Random_NotCount')
main.register_blueprint(Random_More_NotCount_bp, name='Random_More_NotCount')
main.register_blueprint(Select_bp, name='Select')
main.register_blueprint(Select_NotCount_bp, name='Select_NotCount')
main.register_blueprint(search_bp, name='search_bp')

main.register_blueprint(index_bp, name='index')
main.register_blueprint(index_page_bp, name='index_page')

main.register_blueprint(PhotoInfo_bp, name='PhotoInfo')

main.register_blueprint(admin_page_bp, name='admin_page')
main.register_blueprint(admin_AutoTag_page_bp, name='admin_AutoTag_page')
main.register_blueprint(admin_shenhe_page_bp, name='admin_Shenghe_page')
main.register_blueprint(admin_DeletePhoto_bp, name='admin_DeletePhoto')
main.register_blueprint(admin_PassPhoto_bp, name='admin_PassPhoto')
main.register_blueprint(admin_AutoTag_bp, name='admin_AutoTag')

main.register_blueprint(ocss_page_bp, name='ocss_page')

main.config['SSL_CERTIFICATE'] = 'ssl/root-a.top_bundle.crt'
main.config['SSL_PRIVATE_KEY'] = 'ssl/root-a.top.key'

main.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024


# 这个东西到时候要给第一个路由使用

@main.route('/')
def zhuye():
    return render_template('main.html')


@main.route('/ChangeLog')
def ChangeLog():
    return render_template('ChangeLog.html')


@main.route('/Upload')
def 文件上传中心():
    return render_template('upload.html')


@main.route('/survive')
@cross_origin()
def survive():
    return 回调中心.存活报告()


######################################################################
# 自动死亡机制
def 自动死亡线程(调试模式):
    # 自动死亡机制的意思就是自己访问自己
    # 当然是访问存活报告，如果访问不了那么就说明自己在外网上已经死了
    # 那么就自觉的退出，让系统重启自己
    import requests
    print(' * 自动死亡线程：自动死亡线程启动')
    if not 调试模式:
        while True:
            try:
                requests.get('https://root-a.top/survive')
            except:
                print(' * 自动死亡线程：自动死亡机制启动,程序关闭，等待服务端重启')
                # 官方库的重启函数
                if not 调试模式:
                    发送邮件('RandomPhoto主程序：服务器准备重启')
                os.system("sh 重启.sh")
                os._exit(0)
            time.sleep(60 * 2)
    else:
        print(' * 自动死亡线程：调试模式启动，线程退出')


@main.route('/sitemap', methods=['GET'])
def sitemap():
    from Lib.站点地图生成器 import 生成站点地图
    from Lib.programe.重新读取 import 图片信息资源管理器

    生成的XML = 生成站点地图([
        {'图片信息资源': 图片信息资源管理器.站点地图生成器_获取全部图片信息(), '优先级': '0.5', '分类': 'info'},
    ])

    response = make_response(生成的XML)
    response.headers["Content-Type"] = "application/xml"

    return response


@main.route('/robots.txt', methods=['GET'])
def robots():
    return 'User-agent: *'


if __name__ == "__main__":
    main.config['上一次统计'] = {}

    b = threading.Thread(target=审核队列_重新读取, daemon=True)
    c = threading.Thread(target=审核系统缩略图生成器, daemon=True)
    d = threading.Thread(target=自动死亡线程, daemon=True, kwargs={'调试模式': 调试模式()})
    a = threading.Thread(target=重新读取_, daemon=True)

    b.start()
    c.start()
    d.start()
    a.start()

    main.run(host=路径控制.启动位置.启动位置(), port=443, threaded=False,
             ssl_context=(main.config['SSL_CERTIFICATE'], main.config['SSL_PRIVATE_KEY']))
