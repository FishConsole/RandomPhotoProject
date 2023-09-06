from flask import jsonify
from .回调基本模板 import 回调器基本模板

class bgm池:
    @staticmethod
    def 网易云爬虫_成功(数据源):
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = 数据源
        return 回调参数

    @staticmethod
    def 网易云爬虫_文件不存在():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = '文件不存在，填充已发起'
        return 回调参数

    @staticmethod
    def 网易云爬虫_文件索引中():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = '正在填充中，无法完成请求'
        return 回调参数
