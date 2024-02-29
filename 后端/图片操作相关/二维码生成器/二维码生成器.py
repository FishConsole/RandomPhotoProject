import qrcode
import os.path
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 二维码生成器(data, 名字="qrcode", v4模式=False):
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,  # 控制二维码的大小，取值范围为1到40
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 错误纠正水平：L为低、M为中、Q为高、H为最高
        box_size=10,  # 控制二维码中每个小格子的像素数
        border=5,  # 控制二维码边框的格子数
    )
    if v4模式:
        qr.add_data(f"http://{data}:5000")
    else:
        qr.add_data(f"http://[{data}]:5000")
    qr.make(fit=True)

    # 创建一个图片对象
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图片或显示
    img.save(os.path.join(路径控制.前端资源目录().静态资源目录(), "assats", f"{名字}.png"))
