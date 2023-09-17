from flask import jsonify

from .回调基本模板 import 回调器基本模板


class 文件上传器:
    @staticmethod
    def 审核队列_满():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = '审核队列已满，请等待审核完成后再上传。'
        return jsonify(回调参数)

    @staticmethod
    def 没有文件部分():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = '没有文件部分'
        return jsonify(回调参数)

    @staticmethod
    def 未选择文件():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = '未选择文件'
        return jsonify(回调参数)

    @staticmethod
    def 无效的文件类型():
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = '无效的文件类型，只允许上传图片。'
        return jsonify(回调参数)

    @staticmethod
    def 文件大小限制(文件名):
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = f'文件{文件名} 大小超过20MB的限制。'
        return jsonify(回调参数)

    @staticmethod
    def 文件上传成功(文件名):
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'文件 {文件名} 上传成功，人工审核后即可使用。'
        return jsonify(回调参数)
