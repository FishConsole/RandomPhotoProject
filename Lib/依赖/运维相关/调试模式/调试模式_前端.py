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
    if 调试模式():
        return 布尔转换(True)
    else:
        return 布尔转换(admin页面_调试模式_专项)


def ChangeLog_页面调试模式():
    if 调试模式():
        return 布尔转换(True)
    else:
        return 布尔转换(ChangeLog_页面调试模式_专项)


def index页面_调试模式():
    if 调试模式():
        return 布尔转换(True)
    else:
        return 布尔转换(index页面_调试模式_专项)


def main_调试模式():
    if 调试模式():
        return 布尔转换(True)
    else:
        return 布尔转换(启动页_调试模式_专项)


def info_调试模式():
    if 调试模式():
        return 布尔转换(True)
    else:
        return 布尔转换(详情页_调试模式_专项)


def upload_调试模式():
    if 调试模式():
        return 布尔转换(True)
    else:
        return 布尔转换(上传页_调试模式_专项)
