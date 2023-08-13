from PIL import Image


def 图片大小检测(图片路径):
    """
    检测图片大小
    :param 图片路径: 图片路径
    :return: 图片大小
    """
    img = Image.open(图片路径)  # 读取图片
    w, h = img.size  # 获取图片的宽度和高度
    if w > h:
        return "横屏"
    else:
        return "竖屏"
