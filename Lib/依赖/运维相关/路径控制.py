import os
from Lib.依赖.运维相关.调试模式 import *


class 路径控制:
    class 启动位置:
        @staticmethod
        def 启动位置():
            if 调试模式_回环模式() or 调试模式():
                return '127.0.0.1'
            else:
                return '164.155.203.179'

        @staticmethod
        def 域名():
            return 'www.root-a.top'

    @staticmethod
    def 反跨源回调图片_路径():
        return os.path.join('', 'img', '反跨源回调图片')

    @staticmethod
    def 主站原始图片_路径():
        return os.path.join('', 'img', '主站原始图片')

    @staticmethod
    def 主站压缩图片_路径():
        return os.path.join('', 'img', '主站压缩图片')

    @staticmethod
    def 审核系统原始图片_路径():
        return os.path.join('', 'img', '审核系统原始图片')

    @staticmethod
    def 审核系统压缩图片_路径():
        return os.path.join('', 'img', '审核系统压缩图片')

    @staticmethod
    def 审核系统资源图片_路径():
        return os.path.join('', 'img', '审核系统资源图片')

    class 背景音乐_路径:
        @staticmethod
        def 背景音乐_路径_后端():
            return os.path.join('', '', '', '', 'static', 'bgm')

        @staticmethod
        def 背景音乐_路径_前端():
            return os.path.join('static', 'bgm')

    class 缓存目录:
        @staticmethod
        def 缓存目录():
            return os.path.join("Lib", "依赖", "运维相关", "缓存相关")
