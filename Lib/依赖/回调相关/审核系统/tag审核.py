from flask import jsonify
from ..回调基本模板 import 回调器基本模板


class tag审核:
    class 提交请求:
        @staticmethod
        def 提交请求_成功(数据源):
            回调参数 = 回调器基本模板.成功返回模板()
            回调参数['内容'] = f'数据提交成功：{数据源}'
            return 回调参数

        @staticmethod
        def 提交请求_失败(数据源):
            回调参数 = 回调器基本模板.失败返回模板()
            回调参数['内容'] = f'回调数据失败：{数据源}'
            return 回调参数

    class 下一张图片:
        @staticmethod
        def 审核队列已空():
            回调参数 = 回调器基本模板.失败返回模板()
            回调参数['内容'] = f'审核队列没有任何记录'
            return 回调参数
        
        @staticmethod
        def 数据库故障(内容):
            回调参数 = 回调器基本模板.失败返回模板()
            回调参数['内容'] = f'{内容}'
            return 回调参数
        
    class 取消更改:
        @staticmethod
        def 取消更改成功():
            回调参数 = 回调器基本模板.成功返回模板()
            回调参数['内容'] = f'此图片的tag取消更改成功'
            return 回调参数
        
        @staticmethod
        def 取消更改失败():
            回调参数 = 回调器基本模板.成功返回模板()
            回调参数['内容'] = f'此图片的tag取消更改失败'
            return 回调参数