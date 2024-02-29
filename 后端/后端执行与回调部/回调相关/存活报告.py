from flask import jsonify
from .回调基本模板 import 回调器基本模板
from ..执行部门.网络相关.IP获取工具 import *


class 存活报告:
    @staticmethod
    def 存活报告():
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'true'
        回调参数['IPv6地址'] = IPv6获取工具()
        回调参数['IPv4地址'] = IPv4获取工具()
        return jsonify(回调参数)

