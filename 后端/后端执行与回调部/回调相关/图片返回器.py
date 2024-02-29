from flask import jsonify

from .回调基本模板 import 回调器基本模板


class 图片返回器:

    @staticmethod
    def 返回选择的图片_失败():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = f'图片不存在'
        return jsonify(回调参数)

    @classmethod
    def 随机选择的图片_失败(cls):
        pass
