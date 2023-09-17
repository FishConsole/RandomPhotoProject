from .调试模式 import *
from .调试模式_前端 import *


def 调试模式_广播站():
    if 调试模式_回环模式():
        print(' * 调试模式广播站： 现在正在以回环模式运行 [127.0.0.1]')
    if 调试模式_国内模式():
        print(' * 调试模式广播站： 您设置的区域为当前正在 [国内] 服务器上运行')
    if admin_页面调试模式() == 'true':
        print(' * 调试模式广播站：模板 [admin] 正在以调试模式运行')
    if ChangeLog_页面调试模式() == 'true':
        print(' * 调试模式广播站：模板 [ChangeLog] 正在以调试模式运行')
    if index页面_调试模式() == 'true':
        print(' * 调试模式广播站：模板 [index] 正在以调试模式运行')
    if main_调试模式() == 'true':
        print(' * 调试模式广播站：模板 [main] 正在以调试模式运行')
    if info_调试模式() == 'true':
        print(' * 调试模式广播站：模板 [info] 正在以调试模式运行')
    if upload_调试模式() == 'true':
        print(' * 调试模式广播站：模板 [upload]正在以调试模式运行')
    print('-' * 90)
