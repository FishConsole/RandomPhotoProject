import os

from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


# 压缩图片文件
def ResizeImage(输入路径, 输出文件, 目标大小=30, 压缩质量=95, 压缩率=0.9, 原图覆盖基准=4096):  # 通常你只需要修改目标大小
    """不改变图片尺寸压缩到指定大小
    :param 输入路径: 压缩文件输入地址
    :param 输出文件: 压缩文件保存地址
    :param 目标大小: 压缩目标，KB
    :param 压缩率: 每次调整的压缩比率
    :param 压缩质量: 初始压缩比率
    :param 原图覆盖基准: 原图大小超过此值在压缩时会将这张图覆盖掉
    :return: 压缩文件地址，压缩文件大小
    """

    原始大小 = os.path.getsize(输入路径) // 1024  # 函数返回为字节，除1024转为kb（1kb = 1024 bit）

    ImageFile.LOAD_TRUNCATED_IMAGES = True  # 防止图像被截断而报错
    图片 = Image.open(输入路径)
    if 图片.mode == 'RGBA':
        图片 = 图片.convert('RGB')

    # 图片高度,图片宽度 = 图片.size

    图片.save(输出文件)
    计数器 = 0
    if 原始大小 <= 目标大小:
        print(f'图片压缩器：原始文件 {输出文件} 小于目标大小，无需压缩，直接返回')
        图片.save(输出文件)
        return 输出文件

    def 正方形验证(image):
        图片 = Image.open(image)
        图片宽度, 图片高度 = 图片.size
        if 图片宽度 > 图片高度:
            print(f'图片压缩器：图片{image} 宽度：{图片宽度} 大于 图片高度：{图片高度}')
            return 图片宽度 - 图片高度
        elif 图片宽度 < 图片高度:
            print(f'图片{image} 高度：{图片高度} 大于 图片宽度：{图片宽度}')
            return 图片高度 - 图片宽度
        else:
            print(f'图片{image} 宽度: {图片宽度}和高度 {图片高度}相等')
            return 0

    def 垃圾图片验证(image):
        图片 = Image.open(image)
        图片宽度, 图片高度 = 图片.size
        return 图片高度 + 图片宽度 < 2200

    结果 = 正方形验证(输入路径)
    if 结果 < 300:
        print(f'图片压缩库：发现图片{输入路径} 小于200，属于正方形图片，清除')
        os.remove(输入路径)
        return 0

    结果 = 垃圾图片验证(输入路径)
    if 结果:
        print(f'图片压缩库：发现图片{输入路径} 宽度+高度小于2500，属于垃圾图片，清除')
        os.remove(输入路径)
        return 0

    while 原始大小 > 目标大小:
        图片 = Image.open(输出文件)
        宽度, 高度 = 图片.size
        压缩后图片 = 图片.resize((int(宽度 * 压缩率), int(高度 * 压缩率)), Image.ANTIALIAS)  # 最后一个参数设置可以提高图片转换后的质量
        计数器 = 计数器 + 1
        print(f'图片压缩库：压缩图片 {输入路径} 大小 {压缩后图片.size} 超过目标大小 {目标大小}，继续压缩，当前压缩次数 {计数器}')


        try:
            # 如果图片的大小超过4MB，那么压缩到4MB的时候就要覆盖原图，否则就不覆盖
            if 原始大小 > 原图覆盖基准:
                压缩后图片.save(输入路径, quality=压缩质量)
            else:
                压缩后图片.save(输出文件, quality=压缩质量)  # quality为保存的质量，从1（最差）到95（最好），此时为85
        except Exception as e:
            print(e)
            break
        原始大小 = os.path.getsize(输出文件) // 1024
        # time.sleep(0.55)
