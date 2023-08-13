import os


class 路径控制:

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
