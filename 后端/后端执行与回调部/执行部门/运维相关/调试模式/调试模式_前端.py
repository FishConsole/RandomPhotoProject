from .调试模式 import 调试模式

admin页面_调试模式_专项 = False
ChangeLog_页面调试模式_专项 = False
index页面_调试模式_专项 = False
启动页_调试模式_专项 = False
详情页_调试模式_专项 = False
上传页_调试模式_专项 = False


def 布尔转换(值):
    if 值:
        return 'true'
    else:
        return 'false'


def admin_页面调试模式():
    if 调试模式() or admin页面_调试模式_专项 == 'true':
        return 布尔转换(True)
    else:
        return 布尔转换(False)


def ChangeLog_页面调试模式():
    if 调试模式() or ChangeLog_页面调试模式_专项:
        return 布尔转换(True)
    else:
        return 布尔转换(False)


def index页面_调试模式():
    if 调试模式() or index页面_调试模式_专项:
        return 布尔转换(True)
    else:
        return 布尔转换(False)


def main_调试模式():
    if 调试模式() or 启动页_调试模式_专项:
        return 布尔转换(True)
    else:
        return 布尔转换(False)


def info_调试模式():
    if 调试模式() or 详情页_调试模式_专项:
        return 布尔转换(True)
    else:
        return 布尔转换(False)


def upload_调试模式():
    if 调试模式() or 上传页_调试模式_专项:
        return 布尔转换(True)
    else:
        return 布尔转换(False)
