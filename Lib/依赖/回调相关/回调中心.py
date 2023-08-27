from flask import jsonify


class 回调中心:
    @staticmethod
    class 回调器基本模板:
        @staticmethod
        def 成功返回模板():
            """
            - 状态：操作执行成功
            - 内容：要输出的文字
            :return:
            """
            return {'状态': '成功', '内容': '操作执行成功'}

        @staticmethod
        def 失败返回模板():
            """
            - 状态：操作执行失败
            - 内容：要输出的文字
            :return:
            """
            return {'状态': '失败', '内容': '操作执行失败'}

    class bgm池:
        @staticmethod
        def 网易云爬虫_成功(数据源):
            回调参数 = 回调中心.回调器基本模板.成功返回模板()
            回调参数['内容'] = 数据源
            return 回调参数


        @staticmethod
        def 网易云爬虫_文件不存在():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = '文件不存在，填充已发起'
            return 回调参数

        @staticmethod
        def 网易云爬虫_文件索引中():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = '正在填充中，无法完成请求'
            return 回调参数

    class 文件上传器:
        @staticmethod
        def 审核队列_满():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = '审核队列已满，请等待审核完成后再上传。'
            return jsonify(回调参数)

        @staticmethod
        def 没有文件部分():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = '没有文件部分'
            return jsonify(回调参数)

        @staticmethod
        def 未选择文件():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = '未选择文件'
            return jsonify(回调参数)

        @staticmethod
        def 无效的文件类型():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = '无效的文件类型，只允许上传图片。'
            return jsonify(回调参数)

        @staticmethod
        def 文件大小限制(文件名):
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = f'文件{文件名} 大小超过20MB的限制。'
            return jsonify(回调参数)

        @staticmethod
        def 文件上传成功(文件名):
            回调参数 = 回调中心.回调器基本模板.成功返回模板()
            回调参数['内容'] = f'文件 {文件名} 上传成功，人工审核后即可使用。'
            return jsonify(回调参数)

    class 审核系统:
        class 删除审核图片:
            @staticmethod
            def 删除审核图片_成功(图片名字):
                回调参数 = 回调中心.回调器基本模板.成功返回模板()
                回调参数['内容'] = f'删除 {图片名字} 成功'
                return jsonify(回调参数)

            @staticmethod
            def 删除审核图片_失败(图片名字, 错误信息):
                回调参数 = 回调中心.回调器基本模板.失败返回模板()
                回调参数['内容'] = f'删除 {图片名字} 失败'
                回调参数['错误信息'] = 错误信息
                return jsonify(回调参数)

        class 通过审核图片:
            @staticmethod
            def 通过审核图片_成功(图片名字):
                回调参数 = 回调中心.回调器基本模板.成功返回模板()
                回调参数['内容'] = f'通过 {图片名字} 审核成功'
                return jsonify(回调参数)

            @staticmethod
            def 通过审核图片_失败(图片名字, 错误信息):
                回调参数 = 回调中心.回调器基本模板.成功返回模板()
                回调参数['内容'] = f'通过 {图片名字} 审核成功'
                回调参数['错误信息'] = 错误信息
                return jsonify(回调参数)

    class 图片返回器:

        @staticmethod
        def 返回选择的图片_失败():
            回调参数 = 回调中心.回调器基本模板.失败返回模板()
            回调参数['内容'] = f'图片不存在'
            return jsonify(回调参数)

        @classmethod
        def 随机选择的图片_失败(cls):
            pass

    class 自动图像标签生成器:
        pass

    @staticmethod
    def 存活报告():
        回调参数 = 回调中心.回调器基本模板.成功返回模板()
        回调参数['内容'] = f'true'
        return jsonify(回调参数)
