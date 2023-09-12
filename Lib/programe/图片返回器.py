import os
import time
from urllib.parse import urlparse  # 获取链接中域名的一个库

from flask import Blueprint, send_file, render_template, request
from Lib.依赖.图片操作相关.随机图片发生器 import 随机图片发生器
from Lib.依赖.图片操作相关.主页显示器 import home_, home_page_

from Lib.依赖.运维相关.调试模式.调试模式_前端 import *

from Lib.依赖.数据库操作相关.图片信息资源管理器 import 图片信息资源管理器

from Lib.依赖.回调相关.图片返回器 import 图片返回器

from Lib.依赖.杂项.文件读写器 import 文件读写器

from Lib.依赖.运维相关.路径控制 import 路径控制

from Lib.affiliate.密码工具 import 密码工具

# from ..经纬度生成器 import Image_Location

Random_bp = Blueprint('随机图片发生器', __name__)
Random_More_bp = Blueprint('随机图片发生器', __name__)
Random_NotCount_bp = Blueprint('Random_NotCount', __name__)
Random_More_NotCount_bp = Blueprint('Random_NotCount', __name__)

Select_bp = Blueprint('Select', __name__)
Select_NotCount_bp = Blueprint('Select_NotCount', __name__)

index_bp = Blueprint('index', __name__)
index_page_bp = Blueprint('index_page', __name__)

PhotoInfo_bp = Blueprint('PhotoInfo', __name__)

img_bp = Blueprint('img', __name__)

search_bp = Blueprint('admin', __name__)


##########################################
# 站点基本图片显示，给前端使用的
@img_bp.route('/img/<model>/<filename>', methods=['get'])
def img(filename, model):
    # model的意思是模式，这里的意思就是说：这里有五个路径，因此有五个model
    # filename的意思是文件名，这里的意思就是说：指定的路径名
    认可的来源 = ['www.root-a.top', 'root-a.top', '[::1]', b'']
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
            return send_file(os.path.join(路径控制.反跨源回调图片_路径(), "fankuayuan.png"))
        else:
            # 如果现在的时间减去解密得到的时间大于15，那么就是超时了
            if int(time.time()) - int(解密内容) > 60 * 1000:
                return send_file(os.path.join(路径控制.反跨源回调图片_路径(), "fankuayuan.png"))
            else:
                os.system('cls')
    else:
        if 本次来源 not in 认可的来源:
            return send_file(os.path.join(路径控制.反跨源回调图片_路径(), "fankuayuan.png"))

    if model == '主站原始图片':
        return send_file(os.path.join(路径控制.主站原始图片_路径(), filename))

    elif model == 'picture_down':
        return send_file(os.path.join(路径控制.主站压缩图片_路径(), filename))

    elif model == 'temp_files':
        return send_file(os.path.join(路径控制.审核系统原始图片_路径(), filename))

    elif model == 'Temp_File_Start':
        return send_file(os.path.join(路径控制.审核系统压缩图片_路径(), filename))

    else:
        return '404'


##########################################
# 主页
@index_bp.route('/index/', methods=['get'])
def home():
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获得最新上传的图片()
    print(f'压缩图片信息资源: {len(压缩图片信息资源)}')
    return home_(压缩图片信息资源=压缩图片信息资源)


@index_page_bp.route('/index/<page>', methods=['get'])
def home_page(page):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定页数的压缩图片信息资源(page)
    print(压缩图片信息资源)
    return home_page_(page, 压缩图片信息资源)


@PhotoInfo_bp.route('/PhotoInfo/<id>')
def PhotoInfo(id):
    # 从数据库中获得数据

    路径 = os.path.join(路径控制.主站原始图片_路径(), id)
    # 删除路径中可能会出现的斜线
    路径 = 路径.replace('/', '\\')
    # 内容 = 介绍
    # 标签 = Image_Location(os.path.join(路径控制.主站原始图片_路径(), id)).get_image_exif()['拍摄时间']

    标签 = 图片信息资源管理器.获取指定_压缩_图片信息资源(id)[0][1]

    return render_template('PhotoInfo.html',
                           时间=标签[:10],
                           路径=路径,
                           域名=路径控制.启动位置.域名(),
                           调试模式=info_调试模式())


##########################
# ##############################################################
# 接口
########################################################################################

@Random_bp.route('/Random', methods=['get'])
def Random_Random():
    # 判断用户ua，根据用户的ua来选择需要返回的图片

    ua = request.headers.get('User-Agent')
    # 如果是windows或者mac
    if 'Windows' in ua or 'Macintosh' in ua:
        return Random_More_Random('横屏')

    # 如果是安卓
    elif 'Android' in ua:
        if 'Tablet' in ua:
            return Random_More_Random('平板')
        else:
            return Random_More_Random('竖屏')

    # 如果是鸿蒙
    elif 'Harmony' in ua:
        if 'Tablet' in ua:
            return Random_More_Random('平板')
        else:
            return Random_More_Random('竖屏')

    # 如果是ios
    elif 'iPhone' in ua or 'iPad' in ua:
        if 'Tablet' in ua:
            return Random_More_Random('平板')
        else:
            return Random_More_Random('竖屏')


@Random_More_bp.route('/Random/<model>', methods=['get'])
def Random_More_Random(model):
    """
    :param model: model的意思是：强制判断请求所需要的图片，有两种选项，分别返回不同的图片
    :return:
    """
    范围 = request.args.get('range')
    print(范围)
    # 从数据库中获得数据,要原图
    图片 = 随机图片发生器(True, 图片信息资源管理器.获取指定_版式_压缩图片信息资源(model, 范围))
    if not 调试模式():
        上一次统计 = int(文件读写器('上一次统计.txt').读取())
        文件读写器('上一次统计.txt').写入(str(上一次统计 + 1))

    return send_file(图片, mimetype='image/jpg')


########################################################################################

@Random_NotCount_bp.route('/RandomNotCount/')
def Random_RandomNotCount():
    # 判断用户ua，根据用户的ua来选择需要返回的图片

    ua = request.headers.get('User-Agent')
    # 如果是windows或者mac
    if 'Windows' in ua or 'Macintosh' in ua:
        return Random_More_RandomNotCount('横屏')

    # 如果是安卓
    elif 'Android' in ua:
        if 'Tablet' in ua:
            return Random_More_RandomNotCount('平板')
        else:
            return Random_More_RandomNotCount('竖屏')

    # 如果是鸿蒙
    elif 'Harmony' in ua:
        if 'Tablet' in ua:
            return Random_More_RandomNotCount('平板')
        else:
            return Random_More_RandomNotCount('竖屏')

    # 如果是ios
    elif 'iPhone' in ua or 'iPad' in ua:
        if 'Tablet' in ua:
            return Random_More_RandomNotCount('平板')
        else:
            return Random_More_RandomNotCount('竖屏')


@Random_NotCount_bp.route('/RandomNotCount/<model>')
def Random_More_RandomNotCount(model):
    # 从数据库中获得数据
    if model == '横屏':
        图片 = 随机图片发生器(False, 图片信息资源管理器.获取指定_版式_压缩图片信息资源('横屏'))
        return send_file(图片, mimetype='image/jpg')
    elif model == '竖屏':
        图片 = 随机图片发生器(False, 图片信息资源管理器.获取指定_版式_压缩图片信息资源('竖屏'))
        return send_file(图片, mimetype='image/jpg')


########################################################################################


@Select_bp.route('/Select/<filename>')
def Select_select(filename):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定_压缩_图片信息资源(filename)
    if 压缩图片信息资源 != []:
        if not 调试模式():
            上一次统计 = int(文件读写器('上一次统计.txt').读取())
            文件读写器('上一次统计.txt').写入(str(上一次统计 + 1))
        return send_file(os.path.join(路径控制.主站原始图片_路径(), filename))
    else:
        return 图片返回器.返回选择的图片_失败()


@Select_NotCount_bp.route('/SelectNotCount/<filename>')
def Select_SelectNotCount(filename):
    # 从数据库中获得数据
    压缩图片信息资源 = 图片信息资源管理器.获取指定_压缩_图片信息资源(filename)
    if 压缩图片信息资源 != []:
        return send_file(os.path.join(路径控制.主站原始图片_路径(), filename))
    else:
        return 图片返回器.返回选择的图片_失败()


########################################################################################

@search_bp.route('/Search/<tag>')
def Search(tag):
    压缩图片信息资源 = 图片信息资源管理器.搜索压缩图片信息资源(tag)
    # 把压缩图片信息资源中的元组数据类型全部换成列表
    压缩图片信息资源 = [list(i) for i in 压缩图片信息资源]
    print(f'压缩图片信息资源 {压缩图片信息资源}')
    return 压缩图片信息资源
