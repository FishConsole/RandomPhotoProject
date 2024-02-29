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
