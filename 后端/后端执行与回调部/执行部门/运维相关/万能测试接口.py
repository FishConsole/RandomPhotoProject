from flask import Blueprint

from 后端.后端执行与回调部.回调相关.回调基本模板 import 回调器基本模板

universal_bp = Blueprint('universal_bp', __name__)


# 万用接口，请求后会在控制台输出请求的信息
@universal_bp.route('/universal/<test>', methods=['post'])
def universal(test):
    # 参数=request.args.get()
    print('万用测试接口')
    print('-' * 20)
    # print(参数)
    print(test)
    print('-' * 20)
    a = 回调器基本模板.成功返回模板()
    a['图片路径'] = '/Random'
    a['原始标签'] = ['123', '456', '789']
    a['新标签'] = ['000', '111', '222']
    return a
