#####################################
#
# 这是历史版本的图片大小检测函数
#
# def 图片大小检测(图片路径):
#     """
#     检测图片大小
#     :param 图片路径: 图片路径
#     :return: 图片大小
#     """
#
#     # img = Image.open(图片路径)  # 读取图片
#     # w, h = img.size  # 获取图片的宽度和高度
#     # if w > h:
#     #     return "横屏"
#     # else:
#     #     return "竖屏"


def 图片大小检测(图片路径):
    """
    计算图片比例
    :param 图片路径: 图片路径
    :return: 图片比例
    """
    from PIL import Image
    图片 = Image.open(图片路径)
    宽度, 高度 = 图片.size
    宽高比 = 宽度 / 高度
    if 宽高比 > 1.3:
        return f"横屏"
    elif 0.4 < 宽高比 < 0.6:
        return f"竖屏"
    elif 0.6 < 宽高比 < 0.9:
        return f"平板"
    else:
        # 1.0，1.1，1.2 属于正方形图片，这一类图片除了当作头像之外没有任何用处
        # 因此归类为垃圾图片
        return f"垃圾图片"

# print(图片宽高比计算(r"C:\Users\Fish\Pictures\Screenshots\屏幕截图 2023-08-19 200251.png"
#                      ))
