import os


def 强制类型检测(任意变量, 预期类型: list):
    """

    Fishconsole files 强制类型检测

    ----

    - 就是检测目标变量的类型和指定的类型是不是一样的，如果是一样的，就返回ture，如果不是，就返回False

    - 目标类型可根据所加的其他模块自动适应

    :param 任意变量: 你需要比对的变量
    :param 预期类型: 你需要验证的类型比如a=1，强制类型检测（a,'int'）
    :return: bool
    """
    type值 = str(type(预期类型))

    变量类型 = type值.split("'")[1]
    if 变量类型 != "list":
        raise ValueError("强制类型检测》你必须指定list类型的预期类型")

    type值 = str(type(任意变量))
    变量类型 = type值.split("'")[1]
    if 变量类型 in 预期类型:
        return True
    else:
        return False


def 文件存在性检测(文件名: str):
    """

    Fishconsole Fishsys 文件存在性检测模块

    ----

    :param 文件名:你需要检测的文件

    :return: 布尔值
    """
    if not os.path.exists(文件名):
        file = False
    else:
        file = True
    return file


class 配置文件管理器:
    """
    Fishconsole Fishsys 配置文件管理器模块
    ----
    配置文件管理器对象 = 配置文件管理器(文件名)
    print(配置文件管理器.读取变量(配置文件管理器对象, 变量名))  通过key获取value
    print(配置文件管理器.插入变量(配置文件管理器对象, 字典数据)) 通过key插入value
    print(配置文件管理器.覆盖写入(配置文件管理器对象, 字典数据)) 全部删完再写入

    """

    def __init__(self, 文件名: str = 'Fishconsole.fcc'):
        self.文件名 = str(文件名)

    def 数据源重置(self):
        """
        Fishconsole Fishsys 数据源重置模块
        ----
        :return: bool
        """
        with open(f'{self.文件名}', "wb") as file:
            file.write(b"{}")
        return True

    def 覆盖写入(self, 数据):
        文件名 = self.文件名
        a = 强制类型检测(数据, ['dict'])
        if a:
            数据 = str(数据)
            数据 = bytes(数据, encoding="utf-8")
            with open(f'{文件名}', "wb") as file:
                file.write(数据)
        else:
            raise ValueError("Fishconsole IO》模式1》请使用dict的数据", 数据)

    def 读取变量(self, 变量名=None):
        文件名 = self.文件名
        if 文件存在性检测(文件名):
            with open(f'{文件名}', "rb") as file:
                a = file.read()
            解密 = str(a, encoding="utf-8")
            try:
                解密 = eval(解密)
                解密 = dict(解密)

            except SyntaxError:
                配置文件管理器.数据源重置(self)
                print("Fishconsole IO》模式2》变量名提取》操作失败【目标不为dict类型,数据源已重置】", "红色")
                return False

            except NameError:
                配置文件管理器.数据源重置(self)
                raise ValueError("Fishconsole IO》模式2》变量名提取》操作失败【目标被非法篡改,数据源已重置】")

            if 变量名 is None:
                return 解密
            else:
                try:
                    res = 解密.get(变量名)
                    if res is None:
                        # print("变量不存在")
                        return "error"
                    else:
                        return res
                except AttributeError:
                    raise ValueError("Fishconsole IO》模式2》变量名提取》操作失败【未知错误】")
        else:
            # 如果它返回这个布尔值，那就说明它没有检测到这个文件
            # print(logs.日志("Fishconsole IO》模式2》文件没有找到",'红色'))
            return False

    def 插入变量(self, 数据: dict):
        """
        {"键":值}
        :param 数据: {"键":值}
        :return:
        """
        文件名 = self.文件名
        if 文件存在性检测(文件名):
            with open(f'{文件名}', "rb") as file:
                a = file.read()
            解密 = str(a, encoding="utf-8")
            try:
                解密 = eval(解密)
            except SyntaxError:
                配置文件管理器.数据源重置(self)
                print(("Fishconsole IO》模式2》变量名提取》操作失败【目标不为dict类型,数据源已重置】", "红色"))
                return False

            except NameError:
                配置文件管理器.数据源重置(self)
                raise ValueError("Fishconsole IO》模式2》变量名提取》操作失败【目标被非法篡改,数据源已重置】")
            if 强制类型检测(数据, ["dict"]):
                解密 = dict(解密, **数据)
                数据 = str(解密)
                数据 = bytes(数据, encoding="utf-8")
                with open(f'{文件名}', "wb") as file:
                    file.write(数据)
            else:
                raise ValueError("Fishconsole IO》模式3》变量名提取》操作失败【请指定dict类型的数据】")
        else:
            # 如果它返回这个布尔值，那就说明它没有检测到这个文件
            # print("文件没有找到")
            a = 强制类型检测(数据, ['dict'])
            if a:
                数据 = str(数据)
                数据 = bytes(数据, encoding="utf-8")
                with open(f'{文件名}', "wb") as file:
                    file.write(数据)
            else:
                raise ValueError("Fishconsole IO》请使用dict的数据", 数据)
