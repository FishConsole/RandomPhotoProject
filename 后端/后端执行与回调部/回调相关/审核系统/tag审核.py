from ..回调基本模板 import 回调器基本模板


class tag审核:
    @staticmethod
    def tag审核_成功(数据源):
        回调参数 = 回调器基本模板.成功返回模板()
        回调参数['内容'] = f'{数据源}'
        return 回调参数

    @staticmethod
    def tag审核_失败(数据源):
        回调参数 = 回调器基本模板.失败返回模板()
        回调参数['内容'] = f'{数据源}'
        return 回调参数
