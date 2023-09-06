from flask import jsonify
from .回调基本模板 import 回调器基本模板


class 存活报告:
    @staticmethod
    def 存活报告():
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'true'
        return jsonify(回调参数)
