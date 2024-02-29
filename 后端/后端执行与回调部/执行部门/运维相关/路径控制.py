import os
from os.path import dirname

from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import *


def __自动文件夹创建__(路径):
    if 路径控制_开启文件夹自动生成():
        os.makedirs(路径, exist_ok=True)


class 路径控制:
    def __init__(self):
        # core
        self.资源目录基本路径 = os.path.join(dirname(__file__), '..', '..', '..', '..', 'StaticDataCenter')
        # server
        # self.资源目录基本路径 = os.path.join(dirname(__file__), '..', '..', '..', '..', '..', 'StaticDataCenter')

    class 启动位置:

        @staticmethod
        def 启动位置():
            if 调试模式_回环模式() or 调试模式():
                if 开启IPv6():
                    return '::'
                else:
                    return '0.0.0.0'
            else:
                return '0.0.0.0'

        @staticmethod
        def 域名():
            return 'www.root-a.top'

    class 前端资源目录:
        def __init__(self):
            self.资源目录基本路径 = 路径控制().资源目录基本路径

        def 背景音乐_路径_后端(self):
            路径 = os.path.join(self.资源目录基本路径, 'Leading',
                                'LeadingStaticPath',
                                'bgm')
            __自动文件夹创建__(路径)
            return 路径

        def 静态资源目录(self):
            路径 = os.path.join(self.资源目录基本路径, 'Leading',
                                'LeadingStaticPath', 'LeadingStaticPath')
            __自动文件夹创建__(路径)
            return 路径

        def 模板资源目录(self):
            路径 = os.path.join(self.资源目录基本路径, 'Leading',
                                'LeadingStaticPath', 'LeadingTemplatePath')
            __自动文件夹创建__(路径)
            return 路径

        def CallStatistics(self):
            路径 = os.path.join(self.资源目录基本路径, 'AfterEnd',
                                'COUNTER')
            __自动文件夹创建__(路径)
            # try:
            #     with open(os.path.join(路径, 'CallStatistics.txt'), 'r') as f:
            #         CallStatistics = f.read()
            #         if CallStatistics in '':
            #             CallStatistics = 0
            #         f.close()
            # except FileNotFoundError:
            #     with open(os.path.join(路径, 'CallStatistics.txt'), 'a') as f:
            #         f.write('0')
            #         f.close()
            return 路径

        def 分词库(self):
            路径 = os.path.join(self.资源目录基本路径, 'AfterEnd',
                                'WordSegment')
            __自动文件夹创建__(路径)
            return 路径

        def shenhe_token(self):
            路径 = os.path.join(self.资源目录基本路径, 'shenhe_token.txt')
            return 路径

    class 日志目录:
        def __init__(self):
            self.资源目录基本路径 = 路径控制().资源目录基本路径

        def LOGS日志目录(self):
            路径 = os.path.join(self.资源目录基本路径, 'LOG')
            __自动文件夹创建__(路径)
            return 路径

    class Deepdanbooru路径:
        def __init__(self):
            self.资源目录基本路径 = 路径控制().资源目录基本路径

        def Deepdanbooru路径(self):
            路径 = os.path.join(self.资源目录基本路径, 'DeepdanbooruPath')
            __自动文件夹创建__(路径)
            return 路径

    class 临时资源路径:

        def __init__(self):
            self.资源目录基本路径 = 路径控制().资源目录基本路径

        def 临时excel路径(self):
            路径 = os.path.join(self.资源目录基本路径, 'TempData',
                                'Excel')
            __自动文件夹创建__(路径)
            return 路径

    class 图片资源路径:
        class 主站图片资源路径:
            def __init__(self):
                self.资源目录基本路径 = 路径控制().资源目录基本路径

            def 主站原始图片_路径(self):
                路径 = os.path.join(self.资源目录基本路径, 'PictureDatas',
                                    'MainOriginalImage')
                __自动文件夹创建__(路径)
                return 路径

            def 主站压缩图片_路径(self):
                路径 = os.path.join(self.资源目录基本路径, 'PictureDatas',
                                    'MainCompressesImage')
                __自动文件夹创建__(路径)
                return 路径

        class 审核系统图片资源路径:
            def __init__(self):
                self.资源目录基本路径 = 路径控制().资源目录基本路径

            def 审核系统原始图片_路径(self):
                路径 = os.path.join(self.资源目录基本路径, 'PictureDatas',
                                    'AuditSystemOriginImage')
                __自动文件夹创建__(路径)
                return 路径

            def 审核系统压缩图片_路径(self):
                路径 = os.path.join(self.资源目录基本路径, 'PictureDatas',
                                    'AuditSystemCompressesImage')
                __自动文件夹创建__(路径)
                return 路径

    class 反跨源回调图片:
        def __init__(self):
            self.资源目录基本路径 = 路径控制().资源目录基本路径

        def 反跨源回调图片_路径(self):
            路径 = os.path.join(self.资源目录基本路径, 'PictureDatas',
                                'ReverseCallbackPicture')
            __自动文件夹创建__(路径)
            return 路径

    class 数据库路径:
        def __init__(self):
            self.资源目录基本路径 = 路径控制().资源目录基本路径

        def 数据库地址(self):
            路径 = os.path.join(self.资源目录基本路径, 'AfterEnd', 'DataBase',
                                'DataBase.db')
            return 路径


def test路径控制():
    路径控制启动器 = 路径控制()
    ######################################################
    t = 路径控制启动器.前端资源目录().分词库()
    print("分词库:", t, "\n")
    assert os.path.exists(t), True
    t = 路径控制启动器.前端资源目录().静态资源目录()
    print("静态资源目录:", t, "\n")
    assert os.path.exists(t), True
    t = 路径控制启动器.前端资源目录().模板资源目录()
    print("模板资源目录:", t, "\n")
    assert os.path.exists(t), True
    t = 路径控制启动器.前端资源目录().CallStatistics()
    print("CallStatistics:", t, "\n")
    assert os.path.exists(t), True
    ######################################################

    # ######################################################
    t = 路径控制启动器.数据库路径().数据库地址()
    print("数据库地址:", t, "\n")
    assert os.path.exists(t), True
    # ######################################################

    ######################################################
    t = 路径控制启动器.图片资源路径().主站图片资源路径().主站原始图片_路径()
    print("主站原始图片_路径:", t, "\n")
    assert os.path.exists(t), True
    ######################################################

    ######################################################
    t = 路径控制启动器.图片资源路径().审核系统图片资源路径().审核系统原始图片_路径()
    print("审核系统原始图片_路径:", t, "\n")
    assert os.path.exists(t), True
    t = 路径控制启动器.图片资源路径().审核系统图片资源路径().审核系统压缩图片_路径()
    print("审核系统压缩图片_路径:", t, "\n")
    assert os.path.exists(t), True
    ######################################################

    ######################################################
    t = 路径控制启动器.日志目录().LOGS日志目录()
    print("LOGS日志目录:", t, "\n")
    assert os.path.exists(t), True
    t = 路径控制启动器.Deepdanbooru路径().Deepdanbooru路径()
    print("Deepdanbooru路径:", t, "\n")
    assert os.path.exists(t), True
    t = 路径控制启动器.反跨源回调图片().反跨源回调图片_路径()
    print("反跨源回调图片_路径:", t)
    assert os.path.exists(t), True
    ######################################################

    ######################################################
    t = 路径控制启动器.临时资源路径().临时excel路径()
    print("反跨源回调图片_路径:", t)
    assert os.path.exists(t), True
    ######################################################
