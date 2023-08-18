import os
from Lib.programe.调试模式 import *

class 路径控制:
    class 启动位置:
        @staticmethod
        def 启动位置():
            if 调试模式_启动位置() or 调试模式():
                return '127.0.0.1'
            else:
                return '164.155.203.179'

        @staticmethod
        def 域名():
            return 'www.root-a.top'

    @staticmethod
    def 反跨源回调图片_路径():
        return os.path.join('','img', '反跨源回调图片')

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
