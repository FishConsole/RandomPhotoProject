from flask_cors import cross_origin

from 后端.后端执行与回调部.回调相关.存活报告 import 存活报告


@main.route('/survive')
@cross_origin()
def survive():
    return 存活报告.存活报告()