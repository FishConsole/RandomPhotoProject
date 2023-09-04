from flask import Blueprint, request,jsonify

universal_bp = Blueprint('universal_bp',__name__)

# 万用接口，请求后会在控制台输出请求的信息
@universal_bp.route('/universal/<test>', methods=['post'])
def universal(test):
    # 参数=request.args.get()
    print('万用测试接口')
    print('-'*20)
    # print(参数)
    print(test)
    print('-'*20)
    return jsonify({'code':200})