from flask import jsonify
from ..回调基本模板 import 回调器基本模板


class 删除审核图片:
    @staticmethod
    def 删除审核图片_成功(图片名字):
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'删除 {图片名字} 成功'
        return jsonify(回调参数)

    @staticmethod
    def 删除审核图片_失败(图片名字, 错误信息):
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = f'删除 {图片名字} 失败'
        回调参数['错误信息'] = 错误信息
        return jsonify(回调参数)


class 通过审核图片:
    @staticmethod
    def 通过审核图片_成功(图片名字):
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'通过 {图片名字} 审核成功'
        return jsonify(回调参数)

    @staticmethod
    def 通过审核图片_失败(图片名字, 错误信息):
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'通过 {图片名字} 审核成功'
        回调参数['错误信息'] = 错误信息
        return jsonify(回调参数)
